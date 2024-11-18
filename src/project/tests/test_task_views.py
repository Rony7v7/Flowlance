from django.http import HttpResponseForbidden
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from project.models import ProjectMember
from notifications.models import Notification
from ..models import Project, Milestone, Task, TaskDescription, Comment, TaskFile, Application
from profile.models import CompanyProfile , ProfileConfiguration

class TaskViewsTest(TestCase):
    def setUp(self):

        profile_config = ProfileConfiguration.objects.create()
        # Set up the test client, create a user, and log them in
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.company_profile = CompanyProfile.objects.create(user=self.user, company_name='Test Company', nit='1234567890',profileconfiguration = profile_config)
        self.client.login(username='testuser', password='12345')

        # Create a project for testing
        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            requirements="Test Requirements",
            budget=1000,
            start_date="2024-01-01",
            end_date="2024-12-31",
            client=self.user
        )

        # Create an application and accept the user into the project
        self.application = Application.objects.create(
            user=self.user,
            project=self.project,
            status='Aceptada'
        )
        self.project.members.add(self.user)  # Add the user to the project members

        # Create a milestone for testing
        self.milestone = Milestone.objects.create(
            name="Test Milestone",
            description="Milestone Description",
            end_date="2024-11-30",
            project=self.project
        )

        # Create a task for testing
        self.task = Task.objects.create(
            title="Test Task",
            description="Task Description",
            end_date="2024-12-12",
            priority='media',
            state='pendiente',
            milestone=self.milestone,
            responsible=self.user
        )

        # Create a task description for testing
        self.description = TaskDescription.objects.create(
            task=self.task,
            user=self.user,
            content="Initial description content"
        )

        ProjectMember.objects.create(
            project = self.project,
            user = self.user,
            role = "administrator",
            is_owner = True
        )

    def test_create_task_GET(self):
        # Test the GET request to render the page for creating a task
        response = self.client.get(reverse('create_task', args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/task_creation.html')

    def test_create_task_POST_valid(self):
        # Test the POST request to create a task with valid data
        response = self.client.post(reverse('create_task', args=[self.project.id]), {
            'name': 'New Task',
            'description': 'New Task Description',
            'end_date': '2024-12-12',
            'priority': 'media',
            'state': 'pendiente',
            'user': self.user.id,
            'milestone': self.milestone.id
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after creation
        # Assert that the task was created successfully
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_edit_description_GET(self):
        # Test the GET request to edit a task description
        response = self.client.get(reverse('edit_description', args=[self.description.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/edit_description.html')

    def test_edit_description_POST_valid(self):
        # Test the POST request to edit a task description with valid data
        response = self.client.post(reverse('edit_description', args=[self.description.id]), {
            'content': 'Updated description content'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after saving
        self.description.refresh_from_db()
        self.assertEqual(self.description.content, 'Updated description content')

    def test_add_description_POST_valid(self):
        # Test the POST request to add a new description with valid data
        response = self.client.post(reverse('add_description', args=[self.task.id]), {
            'content': 'New description content'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after creation
        self.assertTrue(TaskDescription.objects.filter(content='New description content').exists())

    def test_add_comment_POST_valid(self):
        # Test the POST request to add a comment to a task with valid data
        response = self.client.post(reverse('add_comment', args=[self.task.id]), {
            'content': 'This is a test comment.'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after adding comment
        self.assertTrue(Comment.objects.filter(content='This is a test comment.').exists())

    def test_add_file_POST_valid(self):
        # Create a mock file to upload
        mock_file = SimpleUploadedFile("file.txt", b"file_content", content_type="text/plain")
        response = self.client.post(reverse('add_file', args=[self.task.id]), {
            'file': mock_file
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after file upload
        self.assertTrue(TaskFile.objects.filter(task=self.task).exists())


    def test_update_task_state_valid(self):
        # Prueba para un cambio de estado válido
        response = self.client.post(reverse('update_task_state', args=[self.task.id]), {
            'state': 'completada'
        })

        # Verificar que la tarea se haya actualizado correctamente
        self.task.refresh_from_db()
        self.assertEqual(self.task.state, 'completada')

        # Verificar la redirección después de actualizar el estado
        self.assertEqual(response.status_code, 302)

        # Verificar que la notificación haya sido creada
        self.assertTrue(Notification.objects.filter(
            user=self.task.responsible,
        ).exists())

    def test_update_task_state_unauthorized(self):
        # Crear otro usuario para simular un intento no autorizado de actualizar la tarea
        other_user = User.objects.create_user(username='otheruser', password='12345')
        
        self.client.login(username='otheruser', password='12345')
        ProjectMember.objects.create(
            project = self.project,
            user = other_user,
            role = "administrator",
            is_owner = True
        )
        # Intentar cambiar el estado de la tarea sin ser el responsable
        response = self.client.post(reverse('update_task_state', args=[self.task.id]), {
            'state': 'completada'
        })

        # Verificar que la respuesta sea una prohibición (403 Forbidden)
        self.assertEqual(response.status_code, HttpResponseForbidden.status_code)

        # Verificar que el estado de la tarea no haya cambiado
        self.task.refresh_from_db()
        self.assertNotEqual(self.task.state, 'completada')

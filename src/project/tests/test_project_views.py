from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Project, Milestone, Application


class ProjectViewsTest(TestCase):
    def setUp(self):
        # Set up the test client, create a user and log them in
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Create a project and a milestone for testing
        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            requirements="Test Requirements",
            budget=1000,
            start_date="2024-01-01",
            end_date="2024-12-31",
            client=self.user
        )
        self.milestone = Milestone.objects.create(
            name="Test Milestone",
            description="Milestone Description",
            end_date="2024-11-30",
            project=self.project
        )

    def test_create_project_GET(self):
        # Test the GET request to the create_project view
        response = self.client.get(reverse('create_project'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/create_project.html')

    def test_create_project_POST_valid(self):
        # Test the POST request to create a new project with valid data
        response = self.client.post(reverse('create_project'), {
            'title': 'New Project',
            'description': 'Description for new project',
            'requirements': 'Requirements',
            'budget': 5000,
            'start_date': '2024-01-01',
            'end_date': '2024-12-31'
        })
        self.assertEqual(response.status_code, 302)  # Redirects to the project page
        self.assertTrue(Project.objects.filter(title='New Project').exists())

    def test_my_projects_GET(self):
        # Test the GET request to the my_projects view
        response = self.client.get(reverse('my_projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_list.html')
        self.assertContains(response, self.project.title)

    def test_display_project_GET(self):
        # Test the GET request to display a specific project with the milestone section
        response = self.client.get(reverse('project', args=[self.project.id, 'milestone']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/milestones.html')

    def test_project_list_availableFreelancer_GET(self):
        # Test the GET request to list available projects for freelancers
        response = self.client.get(reverse('available_projectsFreelancer'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_list.html')
        self.assertContains(response, self.project.title)

    def test_project_list_GET(self):
        # Test the GET request to list the projects for the logged-in user
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_main_view.html')
        self.assertContains(response, self.project.title)  # Confirms the project title is present

    def test_project_edit_GET(self):
        # Test the GET request to edit an existing project
        response = self.client.get(reverse('project_edit', args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_form.html')

    def test_project_edit_POST_valid(self):
        # Test the POST request to update a project with valid data
        response = self.client.post(reverse('project_edit', args=[self.project.id]), {
            'title': 'Updated Project Title',
            'description': 'Updated Description',
            'requirements': 'Updated Requirements',
            'budget': 1500,
            'start_date': '2024-01-01',
            'end_date': '2024-12-31'
        })
        self.assertEqual(response.status_code, 302)
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, 'Updated Project Title')

    def test_project_delete_GET(self):
        # Test the GET request to confirm project deletion
        response = self.client.get(reverse('project_delete', args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_delete.html')

    def test_project_delete_POST(self):
        # Test the POST request to delete a project
        response = self.client.post(reverse('project_delete', args=[self.project.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Project.objects.filter(id=self.project.id).exists())

    def test_project_requirements_GET(self):
        # Test the GET request to view project requirements
        response = self.client.get(reverse('project_requirements', args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_requirements.html')

    def test_apply_project_POST(self):
        # Test the POST request to apply for a project
        response = self.client.post(reverse('apply_project', args=[self.project.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Application.objects.filter(user=self.user, project=self.project).exists())

    def test_update_application_status_accept(self):
        # Test the application status update to 'accept'
        application = Application.objects.create(user=self.user, project=self.project)
        response = self.client.post(reverse('update_application_status', args=[application.id, 'accept']))
        self.assertEqual(response.status_code, 302)
        application.refresh_from_db()
        self.assertEqual(application.status, 'Aceptada')

    def test_update_application_status_reject(self):
        # Test the application status update to 'reject'
        application = Application.objects.create(user=self.user, project=self.project)
        response = self.client.post(reverse('update_application_status', args=[application.id, 'reject']))
        self.assertEqual(response.status_code, 302)
        application.refresh_from_db()
        self.assertEqual(application.status, 'Rechazada')

    
    def setUp(self):
        # Configurar el cliente de prueba y crear un usuario
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        # Crear un proyecto para la prueba
        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            requirements="Test Requirements",
            budget=1000,
            start_date="2024-01-01",
            end_date="2024-12-31",
            client=self.user
        )

    def test_data_project_view_redirect_if_not_logged_in(self):
        # Intentar acceder a la vista sin haber iniciado sesión
        response = self.client.get(reverse('data_project', args=[self.project.id]))
        # Debe redirigir al login
        self.assertRedirects(response, f'/accounts/login/?next=/project/{self.project.id}/data_project/')

    def test_data_project_view_logged_in(self):
        # Iniciar sesión
        self.client.login(username='testuser', password='12345')
        
        # Acceder a la vista estando autenticado
        response = self.client.get(reverse('data_project', args=[self.project.id]))

        # Verificar que la respuesta es exitosa (código 200)
        self.assertEqual(response.status_code, 200)
        
        # Verificar que se está utilizando la plantilla correcta
        self.assertTemplateUsed(response, 'projects/data_project.html')

        # Verificar que el contexto contiene el proyecto correcto
        self.assertEqual(response.context['project'], self.project)

    def test_data_project_view_logged_in_invalid_project(self):
        # Iniciar sesión
        self.client.login(username='testuser', password='12345')
        
        # Intentar acceder a un proyecto que no existe
        response = self.client.get(reverse('data_project', args=[9999]))  # ID de proyecto no existente
        
        # Verificar que la respuesta es un 404
        self.assertEqual(response.status_code, 404)
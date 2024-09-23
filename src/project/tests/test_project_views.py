from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Project, Milestone, Application


class ProjectViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Crear un proyecto y un milestone
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
        response = self.client.get(reverse('create_project'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/create_project.html')

    def test_create_project_POST_valid(self):
        response = self.client.post(reverse('create_project'), {
            'title': 'New Project',
            'description': 'Description for new project',
            'requirements': 'Requirements',
            'budget': 5000,
            'start_date': '2024-01-01',
            'end_date': '2024-12-31'
        })
        self.assertEqual(response.status_code, 302)  # Redirección a la página del proyecto
        self.assertTrue(Project.objects.filter(title='New Project').exists())

    def test_my_projects_GET(self):
        response = self.client.get(reverse('my_projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_list.html')  
        self.assertContains(response, self.project.title)


    def test_display_project_GET(self):
        response = self.client.get(reverse('project', args=[self.project.id, 'milestone']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/milestones.html')

    # def test_project_list_availableFreelancer_GET(self):
    #     response = self.client.get(reverse('available_projectsFreelancer'))  
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'projects/project_main_view.html')


    # def test_project_list_GET(self):
    #     response = self.client.get(reverse('project_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'projects/project_list.html')
    #     self.assertContains(response, self.project.title)

    def test_project_detail_GET(self):
        response = self.client.get(reverse('project_detail', args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_detail.html')

    def test_project_edit_GET(self):
        response = self.client.get(reverse('project_edit', args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_form.html')

    def test_project_edit_POST_valid(self):
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
        response = self.client.get(reverse('project_delete', args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_delete.html')

    def test_project_delete_POST(self):
        response = self.client.post(reverse('project_delete', args=[self.project.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Project.objects.filter(id=self.project.id).exists())

    def test_project_requirements_GET(self):
        response = self.client.get(reverse('project_requirements', args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_requirements.html')

    def test_apply_project_POST(self):
        response = self.client.post(reverse('apply_project', args=[self.project.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Application.objects.filter(user=self.user, project=self.project).exists())

    def test_update_application_status_accept(self):
        application = Application.objects.create(user=self.user, project=self.project)
        response = self.client.post(reverse('update_application_status', args=[application.id, 'accept']))
        self.assertEqual(response.status_code, 302)
        application.refresh_from_db()
        self.assertEqual(application.status, 'Aceptada')

    def test_update_application_status_reject(self):
        application = Application.objects.create(user=self.user, project=self.project)
        response = self.client.post(reverse('update_application_status', args=[application.id, 'reject']))
        self.assertEqual(response.status_code, 302)
        application.refresh_from_db()
        self.assertEqual(application.status, 'Rechazada')

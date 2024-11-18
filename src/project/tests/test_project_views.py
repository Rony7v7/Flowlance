from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Project, Milestone, Application
from profile.models import FreelancerProfile, CompanyProfile
from project.forms import ProjectForm
from project.models import ProjectMember

class ProjectViewsTest(TestCase):
    def setUp(self):
        # Crear usuario de empresa y perfil asociado
        self.company_user = User.objects.create_user(username='company_user', password='password123')
        self.company_profile = CompanyProfile.objects.create(user=self.company_user, company_name='Test Company', nit='1234567890')

        # Iniciar sesión con la empresa
        self.client.login(username='company_user', password='password123')

        self.url = reverse('create_project')
        # Create a project and a milestone for testing
        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            requirements="Test Requirements",
            budget=1000,
            start_date="2024-01-01",
            end_date="2024-12-31",
            client=self.company_user
        )
        self.milestone = Milestone.objects.create(
            name="Test Milestone",
            description="Milestone Description",
            end_date="2024-11-30",
            project=self.project
        )

        ProjectMember.objects.create(
            project = self.project,
            user = self.company_user,
            role = "administrator",
            is_owner = True
        )

    def test_create_project_GET(self):
        # Test the GET request to the create_project view
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/create_project.html')
        self.assertIsInstance(response.context['form'], ProjectForm)

    def test_create_project_POST_valid(self):
        # Simula un POST con datos válidos
        data = {
            'title': 'Proyecto Test',
            'description': 'Descripción del proyecto de prueba',
            'requirements': 'Requerimientos del proyecto de prueba',
            'budget': 5000.00,
            'start_date': '2024-10-20',
            'end_date': '2024-11-20'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redirección exitosa
        self.assertRedirects(response, reverse('project', kwargs={'project_id': Project.objects.last().id, 'section': 'milestone'}))
        
        # Verifica que el proyecto fue creado
        self.assertTrue(Project.objects.filter(title = "Proyecto Test").exists())
        project = Project.objects.last()
        self.assertEqual(project.title, 'Proyecto Test')
        self.assertEqual(project.client, self.company_user)
        self.assertIn(self.company_user, project.members.all())

    def test_my_projects_GET(self):
        # Test the GET request to the my_projects view
        response = self.client.get(reverse('my_projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_list_own.html')
        self.assertContains(response, self.project.title)

    def test_display_project_GET(self):
        # Test the GET request to display a specific project with the milestone section
        response = self.client.get(reverse('project', args=[self.project.id, 'milestone']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/management_section/management_section.html')

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
        self.assertFalse(Project.objects.filter(id=self.project.id,is_deleted=False).exists())

    def test_project_requirements_GET(self):
        # Test the GET request to view project requirements
        response = self.client.get(reverse('project_requirements', args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_requirements.html')

    def test_apply_project_POST(self):
        # Test the POST request to apply for a project
        self.freelancer_user = User.objects.create_user(username='freelancer_user', password='password123')
        self.freelancer_profile = FreelancerProfile.objects.create(user=self.freelancer_user, identification='12345678', phone='123456789')
        
        # Iniciar sesión con el freelancer
        self.client.login(username='freelancer_user', password='password123')

        response = self.client.post(reverse('apply_project', args=[self.project.id]))

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Application.objects.filter(user=self.freelancer_user, project=self.project).exists())

    def test_update_application_status_accept(self):
        # Test the application status update to 'accept'
        application = Application.objects.create(user=self.company_user, project=self.project)
        response = self.client.post(reverse('update_application_status', args=[application.id, 'accept']))
        self.assertEqual(response.status_code, 302)
        application.refresh_from_db()
        self.assertEqual(application.status, 'Aceptada')

    def test_update_application_status_reject(self):
        # Test the application status update to 'reject'
        application = Application.objects.create(user=self.company_user, project=self.project)
        response = self.client.post(reverse('update_application_status', args=[application.id, 'reject']))
        self.assertEqual(response.status_code, 302)
        application.refresh_from_db()
        self.assertEqual(application.status, 'Rechazada')

    def test_data_project_view_redirect_if_not_logged_in(self):
        self.client.logout()
        # Intentar acceder a la vista sin haber iniciado sesión
        response = self.client.get(reverse('project', args=[self.project.id,"data_project"]))
        # Debe redirigir al login
        self.assertRedirects(response, f'/login/?next=/project/{self.project.id}/data_project')

    def test_data_project_view_logged_in(self):
        # Iniciar sesión
        self.client.login(username='testuser', password='12345')
        
        # Acceder a la vista estando autenticado
        response = self.client.get(reverse('project', args=[self.project.id,"data_project"]))

        # Verificar que la respuesta es exitosa (código 200)
        self.assertEqual(response.status_code, 200)
        
        # Verificar que se está utilizando la plantilla correcta
        self.assertTemplateUsed(response, 'projects/management_section/management_section.html')

        # Verificar que el contexto contiene el proyecto correcto
        self.assertEqual(response.context['project'], self.project)

    def test_data_project_view_logged_in_invalid_project(self):
        # Iniciar sesión
        self.client.login(username='testuser', password='12345')
        
        # Intentar acceder a un proyecto que no existe
        response = self.client.get(reverse('project', args=[9999,"data_project"]))  # ID de proyecto no existente
        
        # Verificar que la respuesta es un 404
        self.assertEqual(response.status_code, 404)
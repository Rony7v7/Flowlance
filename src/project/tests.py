from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Project
from .forms import ProjectForm

class ProjectViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        
        # Create a sample project
        self.project = Project.objects.create(
            title="Test Project",
            description="This is a test project",
            requirements="Test requirements",
            budget=1000,
            start_date="2024-01-01",
            end_date="2024-12-31",
            client=self.user
        )

    def test_create_project_GET(self):
        response = self.client.get(reverse('create_project'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/create_project.html')
        self.assertIsInstance(response.context['form'], ProjectForm)

    def test_create_project_POST_valid(self):
        project_data = {
            'title': 'New Test Project',
            'description': 'This is a new test project',
            'requirements': 'New test requirements',
            'budget': 2000,
            'start_date': '2024-02-01',
            'end_date': '2024-11-30'
        }
        response = self.client.post(reverse('create_project'), data=project_data)
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertRedirects(response, reverse('my_projects'))
        self.assertTrue(Project.objects.filter(title='New Test Project').exists())

    def test_create_project_POST_invalid(self):
        project_data = {
            'title': '',  # Invalid: Empty title
            'description': 'This is an invalid test project',
            'requirements': 'Invalid test requirements',
            'budget': 'not a number',  # Invalid: Not a number
            'start_date': '2024-02-01',
            'end_date': '2024-11-30'
        }
        response = self.client.post(reverse('create_project'), data=project_data)
        self.assertEqual(response.status_code, 200)  # Should stay on the same page
        self.assertTemplateUsed(response, 'projects/create_project.html')
        self.assertFalse(Project.objects.filter(description='This is an invalid test project').exists())

    def test_my_projects_view(self):
        response = self.client.get(reverse('my_projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/my_projects.html')
        self.assertIn('projects', response.context)
            # Use list to force queryset evaluation and directly compare
        projects_in_context = list(response.context['projects'])
        self.assertEqual(projects_in_context, [self.project])

    def test_login_required_create_project(self):
        self.client.logout()
        response = self.client.get(reverse('create_project'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login page

    def test_login_required_my_projects(self):
        self.client.logout()
        response = self.client.get(reverse('my_projects'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login page

    def test_create_project_sets_client(self):
        project_data = {
            'title': 'Client Test Project',
            'description': 'This is a client test project',
            'requirements': 'Client test requirements',
            'budget': 3000,
            'start_date': '2024-03-01',
            'end_date': '2024-10-31'
        }
        self.client.post(reverse('create_project'), data=project_data)
        created_project = Project.objects.get(title='Client Test Project')
        self.assertEqual(created_project.client, self.user)

        
    def test_multiple_projects_creation_and_retrieval(self):
        # Create multiple projects
        projects_data = [
            {
                'title': f'Project {i}',
                'description': f'Description for Project {i}',
                'requirements': f'Requirements for Project {i}',
                'budget': 1000 + i * 100,
                'start_date': '2024-01-01',
                'end_date': '2024-12-31'
            } for i in range(1, 6)  # Creating 5 projects
        ]

        for project_data in projects_data:
            response = self.client.post(reverse('create_project'), data=project_data)
            self.assertEqual(response.status_code, 302)  # Check for redirect after creation

        # Verify all projects are created
        self.assertEqual(Project.objects.count(), 6)  # 5 new + 1 from setUp

        # Check my_projects view
        response = self.client.get(reverse('my_projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/my_projects.html')

        # Verify all projects are in the context
        projects_in_context = response.context['projects']
        self.assertEqual(len(projects_in_context), 6)

        # Verify details of each project
        for i, project in enumerate(projects_in_context):
            if i == 0:
                # This is the project from setUp
                self.assertEqual(project.title, "Test Project")
            else:
                self.assertEqual(project.title, f'Project {i}')
                self.assertEqual(project.description, f'Description for Project {i}')
                self.assertEqual(project.requirements, f'Requirements for Project {i}')
                self.assertEqual(project.budget, 1000 + i * 100)
                self.assertEqual(str(project.start_date), '2024-01-01')
                self.assertEqual(str(project.end_date), '2024-12-31')

        # Verify all projects belong to the test user
        for project in projects_in_context:
            self.assertEqual(project.client, self.user)

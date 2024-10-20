from project.models import Project, Task
from django.test import TestCase
from django.contrib.auth.models import User
from profile.models import FreelancerProfile
from profile.models import CompanyProfile, Rating

class FreelancerDashboardViewTest(TestCase):
    def setUp(self):
        # Crear usuario freelancer y perfil asociado
        self.freelancer_user = User.objects.create_user(username='freelancer_user', password='password123')
        self.freelancer_profile = FreelancerProfile.objects.create(user=self.freelancer_user, identification='12345678', phone='123456789')
        
        # Iniciar sesión con el freelancer
        self.client.login(username='freelancer_user', password='password123')

    def test_freelancer_dashboard_access(self):
        # Acceder al dashboard como freelancer
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/freelancer_dashboard.html')

    def test_freelancer_projects(self):
        # Crear proyectos y asignar a freelancer
        project1 = Project.objects.create(title="Test Project 1", description="Test Description", client=self.freelancer_user, start_date='2021-01-01', end_date='2021-12-31',budget=1000)
        project1.members.add(self.freelancer_user)

        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('freelancer_projects', response.context)
        self.assertEqual(response.context['freelancer_projects'].count(), 1)

    def test_freelancer_pending_tasks(self):
        # Crear tareas pendientes
        task1 = Task.objects.create(title="Task 1", description="Task description", responsible=self.freelancer_user, state="pendiente",end_date = '2023-12-31')
        
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('freelancer_pending_tasks', response.context)
        self.assertEqual(response.context['freelancer_pending_tasks'].count(), 1)

class CompanyDashboardViewTest(TestCase):
    def setUp(self):
        # Crear usuario de empresa y perfil asociado
        self.company_user = User.objects.create_user(username='company_user', password='password123')
        self.company_profile = CompanyProfile.objects.create(user=self.company_user, company_name='Test Company', nit='1234567890')

        # Iniciar sesión con la empresa
        self.client.login(username='company_user', password='password123')

    def test_company_dashboard_access(self):
        # Acceder al dashboard como empresa
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/company_dashboard.html')

    def test_company_projects(self):
        # Crear proyecto y asignar al usuario empresa
        project1 = Project.objects.create(title="Test Project 1", description="Test Description", client=self.company_user, start_date='2021-01-01', end_date='2021-12-31',budget=1000)
        project1.members.add(self.company_user)
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('company_projects', response.context)
        self.assertEqual(response.context['company_projects'].count(), 1)

    def test_freelancers_associated_with_projects(self):
        # Crear freelancer y asignarlo a un proyecto de la empresa
        freelancer_user = User.objects.create_user(username='freelancer_user', password='password123')
        freelancer_profile = FreelancerProfile.objects.create(user=freelancer_user, identification='987654321', phone='123456789')
        
        project = Project.objects.create(title="Company Project", description="Description", client=self.company_user, start_date='2022-01-01', end_date='2022-12-31',budget=1000)
        project.members.add(self.company_user)
        project.members.add(freelancer_user)

        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('recent_freelancers', response.context)
        self.assertEqual(len(response.context['recent_freelancers']), 1)

    def test_company_ratings_for_freelancers(self):
        # Crear rating para un freelancer
        freelancer_user = User.objects.create_user(username='freelancer_user', password='password123')
        freelancer_profile = FreelancerProfile.objects.create(user=freelancer_user, identification='987654321', phone='123456789')

        Rating.objects.create(freelancer=freelancer_profile, client=self.company_user, stars=5, comment="Excellent work!")

        project = Project.objects.create(title="Company Project", description="Description", client=self.company_user, start_date='2022-01-01', end_date='2022-12-31',budget=1000)
        project.members.add(freelancer_user)

        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('recent_freelancers', response.context)


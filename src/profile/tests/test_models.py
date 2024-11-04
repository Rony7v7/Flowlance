from django.test import TestCase
from django.contrib.auth.models import User
from ..models import (
    FreelancerProfile, Skill, Portfolio, PortfolioProject, 
    Course, WorkExperience, CurriculumVitae, Rating, 
    RatingResponse
)
from django.utils import timezone

class SkillModelTest(TestCase):
    def test_skill_creation(self):
        skill = Skill.objects.create(name='Python', is_custom=False)
        self.assertEqual(str(skill), 'Python')
        self.assertFalse(skill.is_custom)

class FreelancerProfileModelTest(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(username='testuser', password='12345')
        FreelancerProfile.objects.filter(user=self.user).delete()  # Eliminar cualquier perfil existente

    def test_create_freelancer_profile(self):
        profile, created = FreelancerProfile.objects.get_or_create(user=self.user)
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(str(profile), 'testuser')

class PortfolioModelTest(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(username='testuser', password='12345')
        self.profile, created = FreelancerProfile.objects.get_or_create(user=self.user)

    def test_portfolio_creation(self):
        portfolio, created = Portfolio.objects.get_or_create(freelancer_profile=self.profile)
        self.assertEqual(str(portfolio), f"Portfolio of {self.profile}")

class PortfolioProjectModelTest(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(username='testuser', password='12345')
        self.profile, created = FreelancerProfile.objects.get_or_create(user=self.user)
        self.portfolio, created = Portfolio.objects.get_or_create(freelancer_profile=self.profile)

    def test_portfolio_project_creation(self):
        project = PortfolioProject.objects.create(
            portfolio=self.portfolio,
            project_name='Test Project',
            project_description='Project Description',
            start_date=timezone.now().date(),
        )
        self.assertEqual(str(project), 'Test Project')

class CourseModelTest(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(username='testuser', password='12345')
        self.profile, created = FreelancerProfile.objects.get_or_create(user=self.user)
        self.portfolio, created = Portfolio.objects.get_or_create(freelancer_profile=self.profile)

    def test_course_creation(self):
        course = Course.objects.create(
            portfolio=self.portfolio,
            course_name='Test Course',
            organization='Test Organization',
        )
        self.assertEqual(str(course), 'Test Course')

class WorkExperienceModelTest(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(username='testuser', password='12345')
        self.profile, created = FreelancerProfile.objects.get_or_create(user=self.user)

    def test_work_experience_creation(self):
        experience = WorkExperience.objects.create(
            freelancer=self.profile,
            title='Developer',
            company='Test Company',
            start_date=timezone.now().date(),
        )
        self.assertEqual(str(experience), 'Developer en Test Company')

class CurriculumVitaeModelTest(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(username='testuser', password='12345')
        self.profile, created = FreelancerProfile.objects.get_or_create(user=self.user)

    def test_curriculum_vitae_creation(self):
        cv = CurriculumVitae.objects.create(profile=self.profile)
        self.assertEqual(str(cv), f"Curriculum Vitae de {self.profile.user.username}")

class RatingModelTest(TestCase):
    def setUp(self):
        self.client_user, created = User.objects.get_or_create(username='clientuser', password='12345')
        self.freelancer_user, created = User.objects.get_or_create(username='freelanceruser', password='12345')
        self.freelancer_profile, created = FreelancerProfile.objects.get_or_create(user=self.freelancer_user)

    def test_rating_creation(self):
        rating = Rating.objects.create(
            freelancer=self.freelancer_profile,
            client=self.client_user,
            stars=4,
            comment='Great job!'
        )
        self.assertEqual(str(rating), f"{self.client_user.username}'s rating for {self.freelancer_user.username}")

class RatingResponseModelTest(TestCase):
    def setUp(self):
        self.client_user, created = User.objects.get_or_create(username='clientuser', password='12345')
        self.freelancer_user, created = User.objects.get_or_create(username='freelanceruser', password='12345')
        self.freelancer_profile, created = FreelancerProfile.objects.get_or_create(user=self.freelancer_user)
        self.rating, created = Rating.objects.get_or_create(
            freelancer=self.freelancer_profile,
            client=self.client_user,
            stars=4,
            comment='Great job!'
        )

    def test_rating_response_creation(self):
        response = RatingResponse.objects.create(
            rating=self.rating,
            response_text='Thank you!'
        )
        self.assertEqual(response.rating, self.rating)
        self.assertEqual(response.response_text, 'Thank you!')



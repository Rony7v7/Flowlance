from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import (
    FreelancerProfile, Skill, WorkExperience, Rating, RatingResponse, CompanyProfile,ProfileConfiguration
)
from ..forms import AddSkillsForm, AddWorkExperienceForm, RatingForm
from notifications.models import Notification


class FreelancerPlatformTest(TestCase):
    """Test cases for Freelancer Platform covering profiles, notifications, skills, experience, and ratings"""

    def setUp(self):

        profile_config = ProfileConfiguration.objects.create()
        # Create test users
        self.user, _ = User.objects.get_or_create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

        self.client.login(username='testuser', password='12345')

        # Create or get Freelancer profile for the test user
        self.profile, _ = FreelancerProfile.objects.get_or_create(user=self.user, identification="12345", phone="1234567890")

        # Create another user and profile for interaction testing
        self.other_user, _ = User.objects.get_or_create(username='otheruser')
        self.other_user.set_password('12345')
        self.other_user.save()

        self.other_profile, _ = FreelancerProfile.objects.get_or_create(user=self.other_user, identification="54321", phone="0987654321",profileconfiguration = profile_config)

        # Create a notification for testing
        self.notification, _ = Notification.objects.get_or_create(
            user=self.user,
            title = "nuevo titulo",
            link_to_place_of_creation = "link de prueba",
            message="New notification",
            is_read=False
        )

        # Create a rating and response for testing rating deletion
        self.rating = Rating.objects.create(
            freelancer=self.other_profile,
            client=self.user,
            stars=4,
            comment='Good job!'
        )
        self.response = RatingResponse.objects.create(
            rating=self.rating,
            response_text='Thank you!'
        )

    def test_view_own_freelancer_profile(self):
        response = self.client.get(reverse('my_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/freelancer_profile.html')
        self.assertContains(response, self.profile.user.username)

    def test_view_other_user_freelancer_profile_as_company(self):
        # Create a client user with a CompanyProfile
        self.company_user = User.objects.create_user(username='company_user', password='password123')
        self.company_profile = CompanyProfile.objects.create(user=self.company_user, company_name='Test Company', nit='1234567890')

        # Iniciar sesión con la empresa
        self.client.login(username='company_user', password='password123')

        # Perform GET request to view the freelancer profile of another user
        response = self.client.get(reverse('freelancer_profile_view', args=[self.other_profile.user.username]))

        # Check the response
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/freelancer_profile.html')
        self.assertContains(response, self.other_profile.user.username)

    def test_notification_created_on_profile_view(self):

        profile_configuration = ProfileConfiguration.objects.create()

        self.company_user = User.objects.create_user(username='company_user', password='password123')
        self.company_profile = CompanyProfile.objects.create(user=self.company_user, company_name='Test Company', nit='1234567890',profileconfiguration = profile_configuration)

        self.freelancer_user = User.objects.create_user(username='freelancer_user', password='password123')
        self.freelancer_profile = FreelancerProfile.objects.create(user=self.freelancer_user, identification='12345678', phone='123456789',profileconfiguration = profile_configuration)

        # Iniciar sesión con la empresa
        self.client.login(username='company_user', password='password123')

        # Perform the GET request to view the freelancer profile
        response = self.client.get(reverse('freelancer_profile_view', args=[self.freelancer_user.username]))

        # Check if the response was successful
        self.assertEqual(response.status_code, 200)

        # Check if a notification was created for the freelancer
        notification_exists = Notification.objects.filter(
            user=self.freelancer_user,
            title="Perfil visualizado",
        ).exists()

        self.assertTrue(notification_exists, "Notification was not created for the freelancer on profile view.")


    def test_view_notifications(self):
        response = self.client.get(reverse('notifications'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/notifications.html')
        self.assertContains(response, self.notification.message)

    def test_add_skills_view_get(self):
        response = self.client.get(reverse('customize_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/customize_profile.html')
        self.assertIsInstance(response.context['form'], AddSkillsForm)

    def test_add_skills_view_post(self):
        skill = Skill.objects.create(name='Python', is_custom=False)
        response = self.client.post(reverse('customize_profile'), {'predefined_skills': [skill.id]})
        self.assertRedirects(response, reverse('my_profile'))
        self.assertIn(skill, self.profile.skills.all())

    def test_add_experience_view_get(self):
        response = self.client.get(reverse('add_experience'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/add_experience.html')
        self.assertIsInstance(response.context['form'], AddWorkExperienceForm)

    def test_add_experience_view_post(self):
        form_data = {
            'title': 'Developer',
            'company': 'Test Company',
            'start_date': '2022-01-01',
            'end_date': '2022-12-31',
            'description': 'Developed software'
        }
        response = self.client.post(reverse('add_experience'), form_data)
        self.assertRedirects(response, reverse('my_profile'))
        self.assertTrue(WorkExperience.objects.filter(title='Developer').exists())

    def test_add_rating_view_get(self):
        response = self.client.get(reverse('add_rating', args=[self.other_user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/add_rating.html')
        self.assertIsInstance(response.context['form'], RatingForm)

    def test_delete_rating_response_view_post(self):
        response = self.client.post(reverse('delete_rating_response', args=[self.response.id]))
        self.assertRedirects(response, reverse('freelancer_profile', args=[self.user.username]))
        self.assertFalse(RatingResponse.objects.filter(id=self.response.id).exists())


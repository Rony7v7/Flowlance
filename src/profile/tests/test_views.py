from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import (
    FreelancerProfile, Skill, Portfolio, WorkExperience, 
    CurriculumVitae, Rating, RatingResponse, Notification
)
from ..forms import AddSkillsForm, AddWorkExperienceForm, RatingForm, RatingResponseForm

class BaseTestSetup(TestCase):
    """Base setup for all test cases with common setup data"""
    def setUp(self):
        # Create test users
        self.user, _ = User.objects.get_or_create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

        self.client.login(username='testuser', password='12345')
        
        # Create or get profile, avoiding duplicate creation
        self.profile, _ = FreelancerProfile.objects.get_or_create(user=self.user)

        # Create another user for testing interactions
        self.other_user, _ = User.objects.get_or_create(username='otheruser')
        self.other_user.set_password('12345')
        self.other_user.save()

        self.other_profile, _ = FreelancerProfile.objects.get_or_create(user=self.other_user)

        # Create notifications for testing
        self.notification, _ = Notification.objects.get_or_create(
            user=self.user,
            message="New notification",
            is_read=False
        )



class FreelancerProfileViewTest(BaseTestSetup):

    def test_freelancer_profile_view_own_profile(self):
        response = self.client.get(reverse('freelancer_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/freelancer_profile.html')
        self.assertContains(response, self.profile.user.username)

    def test_freelancer_profile_view_other_user_profile(self):
        response = self.client.get(reverse('freelancer_profile_view', args=[self.other_user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/freelancer_profile.html')
        self.assertContains(response, self.other_profile.user.username)


class NotificationViewTest(BaseTestSetup):

    def test_notifications_view(self):
        response = self.client.get(reverse('notifications'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/notifications.html')
        self.assertContains(response, self.notification.message)


class AddSkillsViewTest(BaseTestSetup):

    def test_add_skills_view_get(self):
        response = self.client.get(reverse('customize_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/customize_profile.html')
        self.assertIsInstance(response.context['form'], AddSkillsForm)

    def test_add_skills_view_post(self):
        skill = Skill.objects.create(name='Python', is_custom=False)
        response = self.client.post(reverse('customize_profile'), {'predefined_skills': [skill.id]})
        self.assertRedirects(response, reverse('freelancer_profile'))
        self.assertIn(skill, self.profile.skills.all())


class AddExperienceViewTest(BaseTestSetup):

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
        self.assertRedirects(response, reverse('freelancer_profile'))
        self.assertTrue(WorkExperience.objects.filter(title='Developer').exists())


class AddRatingViewTest(BaseTestSetup):

    def test_add_rating_view_get(self):
        response = self.client.get(reverse('add_rating', args=[self.other_user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/add_rating.html')
        self.assertIsInstance(response.context['form'], RatingForm)


class DeleteRatingResponseViewTest(BaseTestSetup):

    def setUp(self):
        super().setUp()
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

    def test_delete_rating_response_view_post(self):
        response = self.client.post(reverse('delete_rating_response', args=[self.response.id]))
        self.assertRedirects(response, reverse('freelancer_profile'))
        self.assertFalse(RatingResponse.objects.filter(id=self.response.id).exists())


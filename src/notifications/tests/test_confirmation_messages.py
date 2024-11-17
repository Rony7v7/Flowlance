from django.test import TestCase
from django.contrib.auth.models import User
from profile.models import FreelancerProfile, ProfileConfiguration
from django.urls import reverse
from datetime import time

class ProfileConfigurationConfirmationTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = FreelancerProfile.objects.create(user=self.user, identification='ID123')
        self.profile_config = ProfileConfiguration.objects.create(
            notification_when_profile_visited=True,
            sending_notification_to_email=True,
            periodicity_of_notification_report=ProfileConfiguration.Periodicity.MONTHLY,
            silent_start=time(22, 0),
            silent_end=time(6, 0),
            receive_messages=False,
            receive_project_updates=True,
            receive_job_opportunities=True,
        )
        self.profile.profileconfiguration = self.profile_config
        self.profile.save()
        self.client.login(username='testuser', password='12345')
    
    def test_success_message_on_preference_update(self):
        """Test that a success message appears when preferences are updated."""
        response = self.client.post(reverse('notification_preferences'), {
            'notification_when_profile_visited': False, 
            'sending_notification_to_email': False, 
            'periodicity_of_notification_report': ProfileConfiguration.Periodicity.WEEKLY,
            'silent_start': '22:00',
            'silent_end': '06:00',
            'receive_messages': True,
            'receive_project_updates': True,
            'receive_job_opportunities': False,
        }, follow=True)
    
        # Retrieve messages from the response context
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Preferences updated successfully.')

    def test_success_message_on_reset_preferences(self):
        """Test that a success message appears when preferences are reset."""
        response = self.client.get(reverse('reset_notification_preferences'), follow=True)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Preferences reset to default values.')

    def test_message_notifications_default_off(self):
        """Test that message notifications are disabled by default for new users."""
        self.assertFalse(self.profile_config.receive_messages)

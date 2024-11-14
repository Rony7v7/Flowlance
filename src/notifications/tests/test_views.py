from django.test import TestCase
from django.contrib.auth.models import User
from profile.models import FreelancerProfile, ProfileConfiguration
from django.urls import reverse
from datetime import time

class ProfileConfigurationViewTest(TestCase):
    
    def setUp(self):
        # Create user, profile, and profile configuration
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
    
    def test_notification_preference_form_display(self):
        #*Test that the notification preferences form loads correctly.
        response = self.client.get(reverse('notification_preferences'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'silent_start')
        self.assertContains(response, 'silent_end')

    def test_save_notification_preferences(self):
        #*Test that changes in notification preferences are saved and applied immediately.
        response = self.client.post(reverse('notification_preferences'), {
            'notification_when_profile_visited': False, 
            'sending_notification_to_email': False, 
            'periodicity_of_notification_report': ProfileConfiguration.Periodicity.WEEKLY,
            'silent_start': '23:00',
            'silent_end': '07:00',
            'receive_messages': True,
            'receive_project_updates': False,
            'receive_job_opportunities': True,
        })
        
        # Refresh from database to capture changes
        self.profile_config.refresh_from_db()
        
        # Check if the values have been updated correctly
        self.assertFalse(self.profile_config.notification_when_profile_visited)
        self.assertFalse(self.profile_config.sending_notification_to_email)
        self.assertEqual(self.profile_config.periodicity_of_notification_report, ProfileConfiguration.Periodicity.WEEKLY)
        self.assertEqual(self.profile_config.silent_start, time(23, 0))
        self.assertEqual(self.profile_config.silent_end, time(7, 0))

        self.assertTrue(self.profile_config.receive_messages)
        self.assertFalse(self.profile_config.receive_project_updates)
        self.assertTrue(self.profile_config.receive_job_opportunities)
        
        # Check redirection after saving
        self.assertRedirects(response, reverse('notification_preferences'))

    def test_preview_of_selected_notifications(self):
        #*Test that selected notification types show in preview.
        self.profile_config.receive_messages = True
        self.profile_config.receive_project_updates = False
        self.profile_config.receive_job_opportunities = True
        self.profile_config.save()
        response = self.client.get(reverse('notification_preferences'))
        self.assertContains(response, 'Messages')
        self.assertNotContains(response, 'Project Updates')
        self.assertContains(response, 'Job Opportunities')

    def test_reset_notification_preferences(self):
        #*Test that reset action returns preferences to default values.
        self.profile_config.receive_messages = True
        self.profile_config.receive_project_updates = False
        self.profile_config.receive_job_opportunities = False
        self.profile_config.save()
        response = self.client.get(reverse('reset_notification_preferences'))
        self.profile_config.refresh_from_db()
        self.assertTrue(self.profile_config.receive_project_updates)
        self.assertTrue(self.profile_config.receive_job_opportunities)
        self.assertFalse(self.profile_config.receive_messages)
        self.assertRedirects(response, reverse('notification_preferences'))

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profile.models import FreelancerProfile, CompanyProfile, ProfileConfiguration  # Replace 'your_app' with your actual app name
from django.contrib.messages import get_messages

class SettingsViewsTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.freelancer_profile = FreelancerProfile.objects.create(
            user=self.user,
            identification='12345',
            phone='1234567890',
            has_2FA_on=False
        )
        self.settings_url = reverse('account')
        self.security_url = reverse('security')
        self.toggle_2fa_url = reverse('toggle_2fa')

    def test_settings_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.settings_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/account_settings.html')

    def test_settings_view_not_logged_in(self):
        response = self.client.get(self.settings_url)
        self.assertRedirects(response, f'/login/?next={self.settings_url}')

    def test_security_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.security_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/security.html')
        self.assertFalse(response.context['has_2FA_on'])

    def test_security_view_not_logged_in(self):
        response = self.client.get(self.security_url)
        self.assertRedirects(response, f'/login/?next={self.security_url}')

    def test_toggle_2fa_view(self):
        self.client.force_login(self.user)
        
        # Test turning 2FA on
        response = self.client.post(self.toggle_2fa_url, {'has_2FA_on': 'on'})
        self.assertRedirects(response, self.security_url)
        self.freelancer_profile.refresh_from_db()
        self.assertTrue(self.freelancer_profile.has_2FA_on)

        # Test turning 2FA off
        response = self.client.post(self.toggle_2fa_url, {})
        self.assertRedirects(response, self.security_url)
        self.freelancer_profile.refresh_from_db()
        self.assertFalse(self.freelancer_profile.has_2FA_on)

    def test_toggle_2fa_view_not_logged_in(self):
        response = self.client.post(self.toggle_2fa_url, {'has_2FA_on': 'on'})
        self.assertRedirects(response, f'/login/?next={self.toggle_2fa_url}')

    def test_security_no_profile(self):
        # Create a user without a profile
        user_no_profile = User.objects.create_user(username='noprofile', password='12345')
        self.client.force_login(user_no_profile)
        response = self.client.get(self.security_url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['has_2FA_on'])

    def test_toggle_2fa_no_profile(self):
        # Create a user without a profile
        user_no_profile = User.objects.create_user(username='noprofile', password='12345')
        self.client.force_login(user_no_profile)
        response = self.client.post(self.toggle_2fa_url, {'has_2FA_on': 'on'})
        self.assertRedirects(response, self.security_url)
        # Verify that no error occurred even though the user has no profile

class CompanySettingsViewsTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='companyuser', password='12345')
        self.company_profile = CompanyProfile.objects.create(
            user=self.user,
            company_name='Test Company',
            nit='123456789',
            business_type='Test',
            country='Test Country',
            business_vertical='Test Vertical',
            address='Test Address',
            legal_representative='Test Rep',
            phone='1234567890',
            has_2FA_on=False
        )
        self.security_url = reverse('security')
        self.toggle_2fa_url = reverse('toggle_2fa')

    def test_security_view_company(self):
        self.client.force_login(self.user)
        response = self.client.get(self.security_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/security.html')
        self.assertFalse(response.context['has_2FA_on'])

    def test_toggle_2fa_view_company(self):
        self.client.force_login(self.user)
        
        # Test turning 2FA on
        response = self.client.post(self.toggle_2fa_url, {'has_2FA_on': 'on'})
        self.assertRedirects(response, self.security_url)
        self.company_profile.refresh_from_db()
        self.assertTrue(self.company_profile.has_2FA_on)

        # Test turning 2FA off
        response = self.client.post(self.toggle_2fa_url, {})
        self.assertRedirects(response, self.security_url)
        self.company_profile.refresh_from_db()
        self.assertFalse(self.company_profile.has_2FA_on)

class ToggleNotificationToEmailTests(TestCase):
    
    def setUp(self):

        self.profile_config = ProfileConfiguration.objects.create()
        self.profile_config.sending_notification_to_email = False
        self.profile_config.save()

        # Set up a freelancer user with a profile and profile configuration
        self.freelancer_user = User.objects.create_user(username='freelancer_user', password='password123')
        self.freelancer_profile = FreelancerProfile.objects.create(user=self.freelancer_user, identification='12345678', phone='123456789',profileconfiguration = self.profile_config)
        

    def test_toggle_notification_to_email_on(self):
        # Log in as freelancer user to toggle email notification setting
        self.client.login(username='freelancer_user', password='password123')
        
        # Toggle the email notification setting to enable it
        response = self.client.post(reverse('toggle_notification_to_email'), {
            'sending_notification_to_email_variable': 'on'
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Refresh the profile configuration and check if the setting is enabled
        self.profile_config.refresh_from_db()
        self.assertTrue(self.profile_config.sending_notification_to_email, "Email notification setting was not enabled")

    def test_toggle_notification_to_email_off(self):
        # Enable email notification initially
        self.profile_config.sending_notification_to_email = True
        self.profile_config.save()
        
        # Log in as freelancer user to toggle email notification setting
        self.client.login(username='freelancer_user', password='password123')
        
        # Toggle the email notification setting to disable it
        response = self.client.post(reverse('toggle_notification_to_email'), {
            'sending_notification_to_email_variable': 'off'
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Refresh the profile configuration and check if the setting is disabled
        self.profile_config.refresh_from_db()
        self.assertFalse(self.profile_config.sending_notification_to_email, "Email notification setting was not disabled")

class ChangePeriodicityOfNotificationsReportsTest(TestCase):
    def setUp(self):
        # Set up profile configuration
        self.profile_config = ProfileConfiguration.objects.create(
            sending_notification_to_email=False,
            periodicity_of_notification_report=ProfileConfiguration.Periodicity.MONTHLY
        )
        
        # Set up a freelancer user with profile and profile configuration
        self.freelancer_user = User.objects.create_user(username='freelancer_user', password='password123')
        self.freelancer_profile = FreelancerProfile.objects.create(
            user=self.freelancer_user,
            identification='12345678',
            phone='123456789',
            profileconfiguration=self.profile_config
        )
        
        # Login the freelancer user
        self.client.login(username='freelancer_user', password='password123')
        
    def test_change_periodicity_to_weekly(self):
        # Send POST request to change periodicity to 'WEEKLY'
        response = self.client.post(
            reverse('set_periodicity_of_notification_reports'), 
            {'new_periodicity': ProfileConfiguration.Periodicity.WEEKLY}
        )

        # Refresh profile configuration from database
        self.profile_config.refresh_from_db()

        # Check that the periodicity was updated
        self.assertEqual(self.profile_config.periodicity_of_notification_report, ProfileConfiguration.Periodicity.WEEKLY)

        # Check for a success message in the response
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("The periodicity of notification reports has been updated." in str(message) for message in messages))

    def test_invalid_periodicity_choice(self):
        # Send POST request with an invalid periodicity
        response = self.client.post(
            reverse('set_periodicity_of_notification_reports'), 
            {'new_periodicity': 'INVALID'}
        )

        # Ensure the periodicity was not updated
        self.profile_config.refresh_from_db()
        self.assertEqual(self.profile_config.periodicity_of_notification_report, ProfileConfiguration.Periodicity.MONTHLY)

        # Check for an error message in the response
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Invalid periodicity choice." in str(message) for message in messages))
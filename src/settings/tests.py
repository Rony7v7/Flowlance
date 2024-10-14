from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profile.models import FreelancerProfile, CompanyProfile  # Replace 'your_app' with your actual app name

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
        self.settings_url = reverse('account_settings')
        self.security_settings_url = reverse('security_settings')
        self.toggle_2fa_url = reverse('toggle_2fa')

    def test_settings_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.settings_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/account_settings.html')

    def test_settings_view_not_logged_in(self):
        response = self.client.get(self.settings_url)
        self.assertRedirects(response, f'/login/?next={self.settings_url}')

    def test_security_settings_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.security_settings_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/security_settings.html')
        self.assertFalse(response.context['has_2FA_on'])

    def test_security_settings_view_not_logged_in(self):
        response = self.client.get(self.security_settings_url)
        self.assertRedirects(response, f'/login/?next={self.security_settings_url}')

    def test_toggle_2fa_view(self):
        self.client.force_login(self.user)
        
        # Test turning 2FA on
        response = self.client.post(self.toggle_2fa_url, {'has_2FA_on': 'on'})
        self.assertRedirects(response, self.security_settings_url)
        self.freelancer_profile.refresh_from_db()
        self.assertTrue(self.freelancer_profile.has_2FA_on)

        # Test turning 2FA off
        response = self.client.post(self.toggle_2fa_url, {})
        self.assertRedirects(response, self.security_settings_url)
        self.freelancer_profile.refresh_from_db()
        self.assertFalse(self.freelancer_profile.has_2FA_on)

    def test_toggle_2fa_view_not_logged_in(self):
        response = self.client.post(self.toggle_2fa_url, {'has_2FA_on': 'on'})
        self.assertRedirects(response, f'/login/?next={self.toggle_2fa_url}')

    def test_security_settings_no_profile(self):
        # Create a user without a profile
        user_no_profile = User.objects.create_user(username='noprofile', password='12345')
        self.client.force_login(user_no_profile)
        response = self.client.get(self.security_settings_url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['has_2FA_on'])

    def test_toggle_2fa_no_profile(self):
        # Create a user without a profile
        user_no_profile = User.objects.create_user(username='noprofile', password='12345')
        self.client.force_login(user_no_profile)
        response = self.client.post(self.toggle_2fa_url, {'has_2FA_on': 'on'})
        self.assertRedirects(response, self.security_settings_url)
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
        self.security_settings_url = reverse('security_settings')
        self.toggle_2fa_url = reverse('toggle_2fa')

    def test_security_settings_view_company(self):
        self.client.force_login(self.user)
        response = self.client.get(self.security_settings_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/security_settings.html')
        self.assertFalse(response.context['has_2FA_on'])

    def test_toggle_2fa_view_company(self):
        self.client.force_login(self.user)
        
        # Test turning 2FA on
        response = self.client.post(self.toggle_2fa_url, {'has_2FA_on': 'on'})
        self.assertRedirects(response, self.security_settings_url)
        self.company_profile.refresh_from_db()
        self.assertTrue(self.company_profile.has_2FA_on)

        # Test turning 2FA off
        response = self.client.post(self.toggle_2fa_url, {})
        self.assertRedirects(response, self.security_settings_url)
        self.company_profile.refresh_from_db()
        self.assertFalse(self.company_profile.has_2FA_on)

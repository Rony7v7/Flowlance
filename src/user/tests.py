from unittest import mock
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from unittest.mock import patch
from django.utils.translation import gettext as _
from django.contrib.auth.forms import PasswordChangeForm
from profile.models import FreelancerProfile  # Import your profile models

class LoginViewTests(TestCase):
    
    def setUp(self):
        # Set up the test client and create a user
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.login_url = reverse('login')
        self.restore_password_url = reverse('restore_password')

        # Create a FreelancerProfile for the test user
        self.freelancer_profile = FreelancerProfile.objects.create(
            user=self.user,
            identification='12345',
            phone='1234567890',
            has_2FA_on=True  # Set to True to test 2FA flow
        )

    def test_login_view_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')
        self.assertContains(response, 'Email / NIT')

    def test_login_view_POST_valid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': '12345',
        })
        self.assertRedirects(response, '/two_factor_auth/')

    def test_login_view_POST_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(_("Por favor revise su usuario y contraseña") in str(message) for message in messages))

    def test_login_view_POST_empty_fields(self):
        response = self.client.post(self.login_url, {
            'username': '',
            'password': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(_("Por favor revise su usuario y contraseña") in str(message) for message in messages))

    def test_login_view_POST_otp_email_sent(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': '12345',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/two_factor_auth/')
        self.assertEqual(self.client.session['pre_otp_user'], self.user.id)

    @patch('django_otp.oath.TOTP.verify')
    def test_two_factor_validator_success(self, mock_verify):
        mock_verify.return_value = True

        session = self.client.session
        session['pre_otp_user'] = self.user.id
        session.save()

        response = self.client.post(reverse('two_factor_validator'), {
            'otp-code': '123456'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/dashboard/')
        self.assertNotIn('pre_otp_user', self.client.session)

    @patch('django_otp.oath.TOTP.verify')
    def test_two_factor_validator_invalid_otp(self, mock_verify):
        mock_verify.return_value = False

        session = self.client.session
        session['pre_otp_user'] = self.user.id
        session.save()

        response = self.client.post(reverse('two_factor_validator'), {
            'otp-code': 'wrong_code'
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(_("OTP incorrecto"), response.content.decode())

    def test_restore_password_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(self.restore_password_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/restore_password.html')
        self.assertIsInstance(response.context['form'], PasswordChangeForm)

    def test_restore_password_POST_valid(self):
        self.client.force_login(self.user)
        response = self.client.post(self.restore_password_url, {
            'old_password': '12345',
            'new_password1': 'newpassword123',
            'new_password2': 'newpassword123',
        })
        self.assertRedirects(response, reverse('security_settings'))
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(_('Se ha actualizado con exito') in str(message) for message in messages))
        
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newpassword123'))

    def test_restore_password_POST_invalid(self):
        self.client.force_login(self.user)
        response = self.client.post(self.restore_password_url, {
            'old_password': 'wrongoldpassword',
            'new_password1': 'newpassword123',
            'new_password2': 'newpassword123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings/restore_password.html')
        self.assertFalse(response.context['form'].is_valid())

    def test_restore_password_not_logged_in(self):
        response = self.client.get(self.restore_password_url)
        self.assertRedirects(response, f"{reverse('login')}?next={self.restore_password_url}")
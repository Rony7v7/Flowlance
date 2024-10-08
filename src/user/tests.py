from unittest import mock
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from unittest.mock import patch
from django.utils.translation import gettext as _

class LoginViewTests(TestCase):
    
    def setUp(self):
        # Set up the test client and create a user
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.login_url = reverse('login')  # Asegúrate que coincida con tu URL

    def test_login_view_GET(self):
        # Test the GET request to render the login page
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')  # Ensure the correct template is used
        self.assertContains(response, 'Email / NIT')  # Check if the form is rendered correctly

    def test_login_view_POST_valid_credentials(self):
        # Test the POST request with valid credentials
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': '12345',
        })
        self.assertRedirects(response, '/two_factor_auth/')  # Ensure successful login redirects

    def test_login_view_POST_invalid_credentials(self):
        # Test the POST request with invalid credentials
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(("Por favor revise su usuario y contraseña") in str(message) for message in messages))

    def test_login_view_POST_empty_fields(self):
        # Test the POST request with empty fields
        response = self.client.post(self.login_url, {
            'username': '',
            'password': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(_("Por favor revise su usuario y contraseña") in str(message) for message in messages))

    def test_login_view_POST_otp_email_sent(self):
        # Simular un inicio de sesión exitoso y OTP generado
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': '12345',
        })

        # Verificar redirección a la página de 2FA
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/two_factor_auth/')

        # Verificar que el usuario se guardó en la sesión
        self.assertEqual(self.client.session['pre_otp_user'], self.user.id)

    @patch('django_otp.oath.TOTP.verify')  # Mockear la función de verificación OTP
    def test_two_factor_validator_success(self, mock_verify):
        # Simular que el código OTP es verificado con éxito
        mock_verify.return_value = True

        # Crear una sesión con el usuario pre-OTP
        session = self.client.session
        session['pre_otp_user'] = self.user.id
        session.save()

        # Simular la validación de OTP
        response = self.client.post(reverse('two_factor_validator'), {
            'otp-code': '123456'
        })

        # Verificar redirección al dashboard
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/dashboard/')
        self.assertNotIn('pre_otp_user', self.client.session)

    @patch('django_otp.oath.TOTP.verify')  # Mockear la función de verificación OTP
    def test_two_factor_validator_invalid_otp(self, mock_verify):
        # Simular que el código OTP falla
        mock_verify.return_value = False

        # Crear una sesión con el usuario pre-OTP
        session = self.client.session
        session['pre_otp_user'] = self.user.id
        session.save()

        # Simular la validación de OTP fallida
        response = self.client.post(reverse('two_factor_validator'), {
            'otp-code': 'wrong_code'
        })

        # Verificar que el OTP es incorrecto y se muestra el mensaje de error
        self.assertEqual(response.status_code, 200)
        self.assertIn(_("OTP incorrecto"), response.content.decode())
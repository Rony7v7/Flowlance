from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

class LoginViewTests(TestCase):
    def setUp(self):
        # Set up the test client and create a user
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.login_url = reverse('login')  

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
        self.assertRedirects(response, '/dashboard/')  # Ensure successful login redirects to the dashboard

    def test_login_view_POST_invalid_credentials(self):
        # Test the POST request with invalid credentials
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Por favor revise su usuario y contraseña" in str(message) for message in messages))

    def test_login_view_POST_empty_fields(self):
        # Test the POST request with empty fields
        response = self.client.post(self.login_url, {
            'username': '',
            'password': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Por favor revise su usuario y contraseña" in str(message) for message in messages))

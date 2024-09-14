from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class LoginViewTest(TestCase):

    def setUp(self):
        # Create a test user
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )

    def test_login_invalid_credentials(self):
        """Test that invalid credentials display an error message"""
        response = self.client.post(
            reverse("login"), {"username": "wronguser", "password": "wrongpass"}
        )
        self.assertContains(
            response, "Please enter a correct username and password", status_code=200
        )
        self.assertFalse(response.context["form"].is_valid())

    def test_login_empty_form(self):
        """Test that submitting an empty form displays an error"""
        response = self.client.post(reverse("login"), {"username": "", "password": ""})
        self.assertContains(response, "Username is empty", status_code=200)
        self.assertContains(response, "Password is empty", status_code=200)
        self.assertFalse(response.context["form"].is_valid())

    def test_login_success(self):
        """Test that logging in with valid credentials is successful"""
        response = self.client.post(
            reverse("login"), {"username": self.username, "password": self.password}
        )
        self.assertRedirects(
            response, reverse("login")  # TODO: //CHANGE THIS WWHEN HOME IS CREATED
        )  # Assuming success redirects to 'home'
        # After login, user should be authenticated
        self.assertTrue(
            self.client.login(username=self.username, password=self.password)
        )

    def test_login_required_fields(self):
        """Test that 'username' and 'password' fields are required"""
        # Empty username field
        response = self.client.post(
            reverse("login"), {"username": "", "password": self.password}
        )
        self.assertContains(response, "Username is empty", status_code=200)
        self.assertFalse(response.context["form"].is_valid())

        # Empty password field
        response = self.client.post(
            reverse("login"), {"username": self.username, "password": ""}
        )
        self.assertContains(response, "Password is empty", status_code=200)
        self.assertFalse(response.context["form"].is_valid())

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import CompanyProfile


class RegisterViewTest(TestCase):

    def test_freelancer_registration_view(self):
        url = reverse('register_freelancer')
        data = {
            'username': 'freelancer_test',
            'email': 'freelancer@example.com',
            'password1': 'securePassword123!',
            'password2': 'securePassword123!',
            'identification': '1234567890',
            'phone': '3001234567',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='freelancer_test').exists())

    def test_company_registration_view(self):
        url = reverse('register_company')
        data = {
            'username': 'company_test',
            'email': 'company@example.com',
            'password1': 'securePassword123!',
            'password2': 'securePassword123!',
            'company_name': 'Test Company',
            'nit': '9001234567',
            'business_type': 'Tecnología',
            'country': 'Colombia',
            'business_vertical': 'Software',
            'address': 'Calle 123',
            'legal_representative': 'John Doe',
            'phone': '3012345678',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='company_test').exists())

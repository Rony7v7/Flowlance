from django.test import TestCase
from django.contrib.auth.models import User
from ..forms import CompanyRegisterForm
from ..models import CompanyProfile

class CompanyRegisterFormTest(TestCase):
    def test_valid_company_registration(self):
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
        form = CompanyRegisterForm(data)
        self.assertTrue(form.is_valid())
        user = form.save()
        company_profile = CompanyProfile.objects.get(user=user)
        self.assertEqual(company_profile.nit, '9001234567')
        
    def test_company_registration_duplicate_nit(self):
        user = User.objects.create_user(username='existing_company', email='existing@example.com', password='securePassword123!')
        CompanyProfile.objects.create(user=user, company_name='Existing Company', nit='9001234567')
        
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
        
        form = CompanyRegisterForm(data)
        self.assertFalse(form.is_valid())  
        self.assertIn('Este NIT ya está registrado. Por favor, usa otro.', form.errors['nit'])

from django.test import TestCase
from django.contrib.auth.models import User
from ..forms import FreelancerRegisterForm
from ..models import FreelancerProfile
from django.utils.translation import gettext as _

class FreelancerRegisterFormTest(TestCase):
    def test_valid_freelancer_registration(self):
        data = {
            'username': 'freelancer_test',
            'email': 'freelancer@example.com',
            'password1': 'securePassword123!',
            'password2': 'securePassword123!',
            'identification': '1234567890',
            'phone': '3001234567',
        }
        form = FreelancerRegisterForm(data)
        self.assertTrue(form.is_valid())
        user = form.save()
        freelancer_profile = FreelancerProfile.objects.get(user=user)
        self.assertEqual(freelancer_profile.identification, '1234567890')

    def test_freelancer_registration_duplicate_email(self):
        User.objects.create_user(username='existing_user', email='existing@example.com', password='securePassword123!')
        data = {
            'username': 'freelancer_test',
            'email': 'existing@example.com',
            'password1': 'securePassword123!',
            'password2': 'securePassword123!',
            'identification': '1234567890',
            'phone': '3001234567',
        }
        form = FreelancerRegisterForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn(_('Este correo electrónico ya está registrado. Por favor, usa otro.'), form.errors['email'])
#please keep in mind that this _() translates the string insid
    def test_freelancer_registration_duplicate_identification(self):
        user = User.objects.create_user(username='freelancer1', email='freelancer1@example.com', password='securePassword123!')
        FreelancerProfile.objects.create(user=user, identification='1234567890', phone='3001234567')
        
        data = {
            'username': 'freelancer_test',
            'email': 'freelancer2@example.com',
            'password1': 'securePassword123!',
            'password2': 'securePassword123!',
            'identification': '1234567890',
            'phone': '3007654321',
        }
        form = FreelancerRegisterForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn(_('Este ID ya está registrado. Por favor, usa otro.'), form.errors['identification']) #please keep in mind that this _() translates the string insid

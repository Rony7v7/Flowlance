from project.models import Project, Task
from django.test import TestCase
from django.contrib.auth.models import User
from profile.models import FreelancerProfile, CompanyProfile, Rating
from payment.models import Transaction
from django.utils import timezone
import uuid

class FreelancerDashboardViewTest(TestCase):
    def setUp(self):
        self.freelancer_user = User.objects.create_user(username='freelancer_user', password='password123')
        self.freelancer_profile = FreelancerProfile.objects.create(user=self.freelancer_user, identification='12345678', phone='123456789')
        
        self.client.login(username='freelancer_user', password='password123')

        self.transaction1 = Transaction.objects.create(
            freelancer=self.freelancer_user,
            client=User.objects.create_user(username='client1', password='password123'),
            amount=50.00,
            transaction_id=str(uuid.uuid4()),
            status="Success",
            created_at=timezone.now() - timezone.timedelta(days=1)
        )
        self.transaction2 = Transaction.objects.create(
            freelancer=self.freelancer_user,
            client=User.objects.create_user(username='client2', password='password123'),
            amount=150.00,
            transaction_id=str(uuid.uuid4()),
            status="Success",
            created_at=timezone.now()
        )

    def test_freelancer_payment_statistics(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(response.context['max_payment'], 150.00)
        self.assertEqual(response.context['min_payment'], 50.00)
        self.assertEqual(response.context['avg_payment'], 100.00)

    def test_freelancer_last_10_transactions(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

        self.assertIn('last_10_transactions', response.context)
        self.assertEqual(len(response.context['last_10_transactions']), 2)
        self.assertEqual(response.context['last_10_transactions'][0]['amount'], 150.00)
        self.assertEqual(response.context['last_10_transactions'][1]['amount'], 50.00)

class CompanyDashboardViewTest(TestCase):
    def setUp(self):
        self.company_user = User.objects.create_user(username='company_user', password='password123')
        self.company_profile = CompanyProfile.objects.create(user=self.company_user, company_name='Test Company', nit='1234567890')

        self.freelancer_user = User.objects.create_user(username='freelancer_user', password='password123')
        self.freelancer_profile = FreelancerProfile.objects.create(user=self.freelancer_user, identification='987654321', phone='123456789')

        self.transaction1 = Transaction.objects.create(
            freelancer=self.freelancer_user,
            client=self.company_user,
            amount=100.00,
            transaction_id=str(uuid.uuid4()),
            status="Success",
            created_at=timezone.now() - timezone.timedelta(days=1)
        )
        self.transaction2 = Transaction.objects.create(
            freelancer=self.freelancer_user,
            client=self.company_user,
            amount=200.00,
            transaction_id=str(uuid.uuid4()),
            status="Success",
            created_at=timezone.now()
        )

        self.client.login(username='company_user', password='password123')

    def test_company_payment_statistics(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context['max_payment'], 200.00)
        self.assertEqual(response.context['min_payment'], 100.00)
        self.assertEqual(response.context['avg_payment'], 150.00)

    def test_company_payments_by_freelancer(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

        self.assertIn('payments_by_freelancer', response.context)
        payments_by_freelancer = response.context['payments_by_freelancer']
        self.assertEqual(len(payments_by_freelancer), 1)
        self.assertEqual(payments_by_freelancer[0]['freelancer__username'], 'freelancer_user')
        self.assertEqual(payments_by_freelancer[0]['total_paid'], 300.00)

    def test_company_last_10_transactions(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

        self.assertIn('last_10_transactions', response.context)
        self.assertEqual(len(response.context['last_10_transactions']), 2)
        self.assertEqual(response.context['last_10_transactions'][0]['amount'], 100.00)
        self.assertEqual(response.context['last_10_transactions'][1]['amount'], 200.00)

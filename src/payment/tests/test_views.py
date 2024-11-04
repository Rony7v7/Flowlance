from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from project.models import Project, ProjectMember
from payment.models import Transaction
import uuid

class PaymentViewTests(TestCase):
    def setUp(self):
        self.company_user = User.objects.create_user(username='company_user', password='password123')
        self.freelancer_user = User.objects.create_user(username='freelancer_user', password='password123')
        
        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            requirements="Test Requirements",
            budget=1000,
            start_date="2024-01-01",
            end_date="2024-12-31",
            client=self.company_user
        )
        self.project_member = ProjectMember.objects.create(
            project=self.project,
            user=self.freelancer_user,
            role="member"
        )

        self.client = Client()
        self.client.login(username='company_user', password='password123')
        
        self.payment_url = reverse('payment_process', args=[self.project_member.id])
        self.payment_confirm_url = reverse('payment_confirm', args=[str(uuid.uuid4())])

    def test_payment_form_creation(self):
        response = self.client.post(self.payment_url, {
            'paypal_email': 'testpaypal@example.com',
            'amount': '50.00'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('paypal_form', response.context)
        self.assertEqual(response.context['amount'], '50.00')
        
    def test_transaction_creation(self):
        transaction_id = str(uuid.uuid4())
        response = self.client.post(self.payment_url, {
            'paypal_email': 'testpaypal@example.com',
            'amount': '50.00'
        })
        transaction = Transaction.objects.filter(freelancer=self.freelancer_user, client=self.company_user).first()
        
        self.assertIsNotNone(transaction)
        self.assertEqual(transaction.amount, 50.00)
        self.assertEqual(transaction.status, "Pending")
        self.assertEqual(transaction.client, self.company_user)  
        self.assertEqual(transaction.freelancer, self.freelancer_user)  
    def test_payment_confirm(self):
        transaction_id = str(uuid.uuid4())
        transaction = Transaction.objects.create(
            client=self.company_user,
            freelancer=self.freelancer_user,
            amount=50.00,
            transaction_id=transaction_id,
            status="Pending"
        )
        response = self.client.get(reverse('payment_confirm', args=[transaction_id]))
        transaction.refresh_from_db()  
        
        self.assertEqual(transaction.status, "Success")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "payment/payment_success.html")

    def test_filter_transactions_by_amount(self):
        Transaction.objects.create(
            client=self.company_user,
            freelancer=self.freelancer_user,
            amount=50.00,
            transaction_id=str(uuid.uuid4()),
            status="Pending",
            created_at=timezone.now()
        )
        Transaction.objects.create(
            client=self.company_user,
            freelancer=self.freelancer_user,
            amount=100.00,
            transaction_id=str(uuid.uuid4()),
            status="Success",
            created_at=timezone.now()
        )
        
        response = self.client.get(self.payment_url, {
            'min_amount': '60.00',
            'max_amount': '150.00'
        })
        transactions = response.context['transactions']
        
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].amount, 100.00)

    def test_filter_transactions_by_date(self):
        Transaction.objects.create(
            client=self.company_user,
            freelancer=self.freelancer_user,
            amount=50.00,
            transaction_id=str(uuid.uuid4()),
            status="Pending",
            created_at=timezone.now() - timezone.timedelta(days=10)
        )
        Transaction.objects.create(
            client=self.company_user,
            freelancer=self.freelancer_user,
            amount=75.00,
            transaction_id=str(uuid.uuid4()),
            status="Success",
            created_at=timezone.now()
        )

        start_date = (timezone.now() - timezone.timedelta(days=5)).date()
        end_date = timezone.now().date()
        response = self.client.get(self.payment_url, {
            'start_date': start_date,
            'end_date': end_date
        })
        transactions = response.context['transactions']
        
        self.assertEqual(len(transactions), 2)  
        self.assertEqual(transactions[0].amount, 50.00)

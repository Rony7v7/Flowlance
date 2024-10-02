from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Assigment, Milestone, Project


class AssigmentViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            requirements="Test Requirements",
            budget=1000,
            start_date="2024-01-01",
            end_date="2024-12-31",
            client=self.user
        )
        self.project.members.add(self.user)
        self.milestone = Milestone.objects.create(
            name="Test Milestone",
            description="Test Description",
            end_date="2024-11-30",
            project=self.project
        )
        self.assigment = Assigment.objects.create(
            title="Initial Assignment",
            description="Initial Description",
            milestone=self.milestone,
            responsible=self.user,
            creator=self.user,
            end_date="2024-10-01",
        )

    def test_create_assigment_GET(self):
        response = self.client.get(reverse('create_assigment', args=[self.milestone.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/create_assigment.html')
        self.assertIn('id="name"', response.content.decode()) 
        self.assertIn('id="description"', response.content.decode()) 
        self.assertIn('id="user"', response.content.decode())  
        self.assertIn('id="end_date"', response.content.decode()) 

    def test_create_assigment_POST_valid(self):
        response = self.client.post(reverse('create_assigment', args=[self.milestone.id]), {
            'name': 'Test Assignment',
            'description': 'Assignment Description',
            'end_date': '2024-10-01',
            'user': self.user.id
        })
        self.assertEqual(response.status_code, 302)  # Redirecciona correctamente
        self.assertTrue(Assigment.objects.filter(title='Test Assignment').exists())

    def test_edit_assigment_GET(self):
        response = self.client.get(reverse('edit_assigment', args=[self.assigment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/create_assigment.html')
        self.assertIn('value="Initial Assignment"', response.content.decode()) 

    def test_edit_assigment_POST_valid(self):
        response = self.client.post(reverse('edit_assigment', args=[self.assigment.id]), {
            'name': 'Updated Assignment',
            'description': 'Updated Description',
            'end_date': '2024-12-01',
            'user': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assigment.refresh_from_db()
        self.assertEqual(self.assigment.title, 'Updated Assignment')

    def test_delete_assigment_POST(self):
        response = self.client.post(reverse('delete_assigment', args=[self.assigment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Assigment.objects.filter(id=self.assigment.id,is_deleted=False).exists())

    def test_upload_assigment_GET(self):
        response = self.client.get(reverse('upload_assigment', args=[self.assigment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/upload_assigment_file.html')


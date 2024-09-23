from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Project, Milestone


class MilestoneViewsTest(TestCase):
    def setUp(self):
        # Set up the test client, create a user, and log them in
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Create a project for testing
        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            requirements="Test Requirements",
            budget=1000,
            start_date="2024-01-01",
            end_date="2024-12-31",
            client=self.user
        )

        # Create a milestone for testing
        self.milestone = Milestone.objects.create(
            name="Test Milestone",
            description="Milestone Description",
            end_date="2024-11-30",
            project=self.project
        )

    def test_add_milestone_POST_valid(self):
        # Test the POST request to add a new milestone with valid data
        response = self.client.post(reverse('add_milestone', args=[self.project.id]), {
            'name': 'New Milestone',
            'description': 'New Milestone Description',
            'end_date': '2024-10-15'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after creation
        self.assertTrue(Milestone.objects.filter(name='New Milestone').exists())  # Milestone should be created

    def test_add_milestone_POST_invalid(self):
        # Test the POST request to add a milestone with invalid data (empty fields)
        response = self.client.post(reverse('add_milestone', args=[self.project.id]), {
            'name': '',
            'description': '',
            'end_date': '2024-10-15'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect due to invalid input
        self.assertFalse(Milestone.objects.filter(name='').exists())  # Milestone should not be created

    def test_edit_milestone_GET(self):
        # Test the GET request to render the page for editing an existing milestone
        response = self.client.get(reverse('edit_milestone', args=[self.milestone.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/manage_milestone.html')
        
        # Check that the context has 'is_editing' set to True
        self.assertTrue(response.context['is_editing'])


    def test_edit_milestone_POST_valid(self):
        # Test the POST request to update an existing milestone with valid data
        response = self.client.post(reverse('edit_milestone', args=[self.milestone.id]), {
            'name': 'Updated Milestone',
            'description': 'Updated Description',
            'end_date': '2024-12-01',
            'start_date': '2024-01-01'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after update
        self.milestone.refresh_from_db()
        self.assertEqual(self.milestone.name, 'Updated Milestone')  # Check if the milestone is updated

    def test_edit_milestone_POST_invalid(self):
        # Test the POST request to update a milestone with invalid data (empty fields)
        response = self.client.post(reverse('edit_milestone', args=[self.milestone.id]), {
            'name': '',
            'description': '',
            'end_date': '2024-12-01',
            'start_date': '2024-01-01'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect due to invalid input
        self.milestone.refresh_from_db()
        self.assertNotEqual(self.milestone.name, '')  # Milestone should not be updated with invalid data

    def test_delete_milestone_POST(self):
        # Test the POST request to actually delete the milestone
        response = self.client.post(reverse('delete_milestone', args=[self.milestone.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect after deletion
        self.assertFalse(Milestone.objects.filter(id=self.milestone.id).exists())  # Milestone should be deleted

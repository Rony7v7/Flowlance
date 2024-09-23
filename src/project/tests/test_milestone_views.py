# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth.models import User
# from ..models import Project, Milestone


# class MilestoneViewsTest(TestCase):
#     def setUp(self):
#         # Set up the test client, create a user, and log them in
#         self.client = Client()
#         self.user = User.objects.create_user(username='testuser', password='12345')
#         self.client.login(username='testuser', password='12345')

#         # Create a project for testing
#         self.project = Project.objects.create(
#             title="Test Project",
#             description="Test Description",
#             requirements="Test Requirements",
#             budget=1000,
#             start_date="2024-01-01",
#             end_date="2024-12-31",
#             client=self.user
#         )

#         # Create a milestone for testing
#         self.milestone = Milestone.objects.create(
#             name="Test Milestone",
#             description="Milestone Description",
#             end_date="2024-11-30",
#             project=self.project
#         )

#     def test_add_milestone_GET(self):
#         # Test the GET request to add a new milestone
#         response = self.client.get(reverse('add_milestone', args=[self.project.id]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'projects/manage_milestone.html')

#     def test_add_milestone_POST_valid(self):
#         # Test the POST request to add a new milestone with valid data
#         response = self.client.post(reverse('add_milestone', args=[self.project.id]), {
#             'name': 'New Milestone',
#             'description': 'New Milestone Description',
#             'end_date': '2024-10-15'
#         })
#         self.assertEqual(response.status_code, 302)  # Should redirect after creation
#         self.assertTrue(Milestone.objects.filter(name='New Milestone').exists())

#     def test_add_milestone_POST_invalid(self):
#         # Test the POST request with invalid data (empty fields)
#         response = self.client.post(reverse('add_milestone', args=[self.project.id]), {
#             'name': '',
#             'description': '',
#             'end_date': '2024-10-15'
#         })
#         self.assertEqual(response.status_code, 302)  # Redirect due to invalid input
#         self.assertFalse(Milestone.objects.filter(name='').exists())
#         # Test the GET request to confirm the deletion of a milestone
#         response = self.client.get(reverse('delete_milestone', args=[self.milestone.id]))
#         self.assertEqual(response.status_code, 200)

#     def test_delete_milestone_POST(self):
#         # Test the POST request to delete a milestone
#         response = self.client.post(reverse('delete_milestone', args=[self.milestone.id]))
#         self.assertEqual(response.status_code, 302)  # Should redirect after deletion
#         self.assertFalse(Milestone.objects.filter(id=self.milestone.id).exists())

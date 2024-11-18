from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from project.models import Event, Project
from profile.models import CompanyProfile, ProfileConfiguration
from django.utils import timezone
from datetime import datetime

class AllEventsViewTest(TestCase):
    def setUp(self):
        self.profile_config, _ = ProfileConfiguration.objects.get_or_create()
        self.profile_config.notification_when_profile_visited = False
        self.profile_config.save()
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.company_profile = CompanyProfile.objects.create(user=self.user, company_name='Test Company', nit='1234567890',profileconfiguration = self.profile_config)
        self.project = Project.objects.create(
            title="Test Project",
            description="Project description",
            budget=1000.00,
            start_date="2024-01-01",
            end_date="2024-12-31",
            client=self.user
        )
        # Parse the string into a naive datetime
        start_naive = datetime.strptime("2024-01-10T10:00:00", "%Y-%m-%dT%H:%M:%S")
        end_naive = datetime.strptime("2024-01-10T12:00:00", "%Y-%m-%dT%H:%M:%S")

        # Convert the naive datetime to a time zone-aware datetime
        start_aware = timezone.make_aware(start_naive)
        end_aware = timezone.make_aware(end_naive)

        # Now, use these aware datetime objects to create the event
        self.event = Event.objects.create(
            name="Test Event",
            start=start_aware,
            end=end_aware,
            project=self.project
        )
        self.client.login(username='testuser', password='12345')

    
    def test_invalid_project_id(self):
        response = self.client.get(reverse('all_events'), {'project_id': 'invalid'})
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {'error': 'Invalid project ID'})

    def test_no_project_id(self):
        response = self.client.get(reverse('all_events'))
        self.assertEqual(response.status_code, 400)
    
    def test_valid_project_id(self):
        response = self.client.get(reverse('all_events'), {'project_id': self.project.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Event', str(response.content))


class EditEventViewTest(TestCase):
    def setUp(self):
        self.profile_config, _ = ProfileConfiguration.objects.get_or_create()
        self.profile_config.notification_when_profile_visited = False
        self.profile_config.save()
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.company_profile = CompanyProfile.objects.create(user=self.user, company_name='Test Company', nit='1234567890',profileconfiguration = self.profile_config)
        self.project = Project.objects.create(
            title="Test Project",
            description="Project description",
            budget=1000.00,
            start_date="2024-01-01",
            end_date="2024-12-31",
            client=self.user
        )
        # Parse the string into a naive datetime
        start_naive = datetime.strptime("2024-01-10T10:00:00", "%Y-%m-%dT%H:%M:%S")
        end_naive = datetime.strptime("2024-01-10T12:00:00", "%Y-%m-%dT%H:%M:%S")

        # Convert the naive datetime to a time zone-aware datetime
        start_aware = timezone.make_aware(start_naive)
        end_aware = timezone.make_aware(end_naive)

        # Now, use these aware datetime objects to create the event
        self.event = Event.objects.create(
            name="Test Event",
            start=start_aware,
            end=end_aware,
            project=self.project
        )
        self.client.login(username='testuser', password='12345')

    def test_edit_event_success(self):
        response = self.client.post(reverse('edit_event', args=[self.event.id]), {
            'name': 'Updated Event',
            'start': '2024-01-15T10:00:00',
            'end': '2024-01-15T12:00:00',
            'description': 'Updated description'
        })
        self.assertEqual(response.status_code, 200)
        self.event.refresh_from_db()
        self.assertEqual(self.event.name, 'Updated Event')
        self.assertEqual(self.event.description, 'Updated description')

    def test_edit_event_invalid_data(self):
        response = self.client.post(reverse('edit_event', args=[self.event.id]), {
            'name': '',  # Name is required
            'start': 'invalid-date',  # Invalid date format
            'end': '2024-01-15T12:00:00'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('errors', response.json())


class DisplayProjectViewTest(TestCase):
    def setUp(self):
        self.profile_config, _ = ProfileConfiguration.objects.get_or_create()
        self.profile_config.notification_when_profile_visited = False
        self.profile_config.save()
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.company_profile = CompanyProfile.objects.create(user=self.user, company_name='Test Company', nit='1234567890',profileconfiguration = self.profile_config)
        self.project = Project.objects.create(
            title="Test Project",
            description="Project description",
            budget=1000.00,
            start_date="2024-01-01",
            end_date="2024-12-31",
            client=self.user
        )
         # Parse the string into a naive datetime
        start_naive = datetime.strptime("2024-01-10T10:00:00", "%Y-%m-%dT%H:%M:%S")
        end_naive = datetime.strptime("2024-01-10T12:00:00", "%Y-%m-%dT%H:%M:%S")

        # Convert the naive datetime to a time zone-aware datetime
        start_aware = timezone.make_aware(start_naive)
        end_aware = timezone.make_aware(end_naive)

        # Now, use these aware datetime objects to create the event
        self.event = Event.objects.create(
            name="Test Event",
            start=start_aware,
            end=end_aware,
            project=self.project
        )
        self.client.login(username='testuser', password='12345')

    def test_display_project_not_found(self):
        response = self.client.get(reverse('project', args=[9999, 'calendar']))
        self.assertEqual(response.status_code, 404)

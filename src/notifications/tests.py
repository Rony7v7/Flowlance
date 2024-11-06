from django.test import TestCase , Client
from django.contrib.auth.models import User
from django.urls import reverse
from profile.models import CompanyProfile, FreelancerProfile, ProfileConfiguration
from .models import Notification
from .utils import send_notification
from .models import Notification

class NotificationTests(TestCase):
    def setUp(self):

        self.profile_config, _ = ProfileConfiguration.objects.get_or_create()
        self.profile_config.notification_when_profile_visited = False
        self.profile_config.save()
        # Create a user for testing
        self.user = User.objects.create(username="testuser", password="password123")

        self.company_user = User.objects.create_user(username='company_user', password='password123')
        self.company_profile = CompanyProfile.objects.create(user=self.company_user, company_name='Test Company', nit='1234567890',profileconfiguration = self.profile_config)
        
        self.freelancer_user = User.objects.create_user(username='freelancer_user', password='password123')
        self.freelancer_profile = FreelancerProfile.objects.create(user=self.freelancer_user, identification='12345678', phone='123456789', profileconfiguration = self.profile_config)
        
        # Create a ProfileConfiguration for the freelancer with notification disabled by default

    def test_notification_creation(self):
        # Call the send_notification function
        notification_message = "Test notification message"
        notification_title = "test notification"
        notification_link = "test link"
        send_notification(notification_title,notification_message,notification_link, self.user)

        # Verify that a Notification object was created for the user
        notification_exists = Notification.objects.filter(user=self.user, message=notification_message).exists()
        self.assertTrue(notification_exists)

    def test_notification_message_content(self):
        # Test if the created notification has the correct message content
        notification_message = "Test message for content verification"
        notification_title = "test notification"
        notification_link = "test link"
        send_notification(notification_title,notification_message,notification_link, self.user)

        notification = Notification.objects.get(user=self.user, message=notification_message)
        self.assertEqual(notification.message, notification_message)

        
    def test_toggle_notification_setting(self):
        # Log in as freelancer user to toggle notification setting
        self.client.login(username='freelancer_user', password='password123') 
        self.profile_config.notification_when_profile_visited = True

        
        # Toggle the notification setting to enable it
        response = self.client.post(reverse('toggle_notification_when_profile_visited'), {
            'notification_when_profile_visited_variable': 'on'
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Refresh the profile config and check if the setting is enabled
        self.profile_config.refresh_from_db()
        self.assertTrue(self.profile_config.notification_when_profile_visited, "Notification setting was not enabled")

        # Toggle the notification setting to disable it again
        response = self.client.post(reverse('toggle_notification_when_profile_visited'), {
            'notification_when_profile_visited_variable': 'off'
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Refresh the profile config and check if the setting is disabled
        self.profile_config.refresh_from_db()
        self.assertFalse(self.profile_config.notification_when_profile_visited, "Notification setting was not disabled")

    def test_notification_created_on_profile_view(self):
        # Enable notification setting for freelancer
        self.profile_config.notification_when_profile_visited = True
        self.profile_config.save()
        
        # Log in as the company user to view freelancer profile
        self.client.login(username='company_user', password='password123')

        # Perform the GET request to view the freelancer profile
        response = self.client.get(reverse('freelancer_profile_view', args=[self.freelancer_user.username]))
        
        # Check if the response was successful
        self.assertEqual(response.status_code, 200)

        # Check if a notification was created for the freelancer
        notification_exists = Notification.objects.filter(
            user=self.freelancer_user,
            title="Perfil visualizado",
        ).exists()
        self.assertTrue(notification_exists, "Notification was not created for the freelancer on profile view.")

    def test_notification_not_created_when_disabled(self):
        # Ensure notification setting is disabled for freelancer
        self.profile_config.notification_when_profile_visited = False
        self.profile_config.save()

        # Log in as the company user to view freelancer profile
        self.client.login(username='company_user', password='password123')

        # Perform the GET request to view the freelancer profile
        response = self.client.get(reverse('freelancer_profile_view', args=[self.freelancer_user.username]))
        
        # Check if the response was successful
        self.assertEqual(response.status_code, 200)

        # Check that no notification was created for the freelancer
        notification_exists = Notification.objects.filter(
            user=self.freelancer_user,
            title="Perfil visualizado",
        ).exists()
        self.assertFalse(notification_exists, "Notification should not be created when the setting is disabled.")

class NotificationModelTest(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username="testuser", password="password")
        self.client.force_login(self.user)  # Ensures user is logged in without delay

        self.notification1 = Notification.objects.create(
            user=self.user, title="Notification 1", message="Message 1", is_read=False
        )
        self.notification2 = Notification.objects.create(
            user=self.user, title="Notification 2", message="Message 2", is_read=False
        )

    def test_notification_creation(self):
        notification = Notification.objects.create(
            user=self.user,
            message='New notification message',
        )
        self.assertEqual(str(notification), f"Notification for {self.user.username}: New notification message")
        self.assertFalse(notification.is_read)

    def test_mark_notification_as_read_success(self):
        # Send a POST request to mark the first notification as read
        response = self.client.post(reverse("mark-as-read", args=[self.notification1.id]))
        
        # Check the response status code and JSON content
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "success", "message": "Notification marked as read."})
        
        # Verify that the notification is marked as read in the database
        self.notification1.refresh_from_db()
        self.assertTrue(self.notification1.is_read)

    def test_mark_notification_as_read_not_found(self):
        # Attempt to mark a non-existent notification as read
        response = self.client.post(reverse("mark-as-read", args=[999]))
        
        # Check for a 404 response
        self.assertEqual(response.status_code, 404)

    def test_mark_notification_as_read_invalid_method(self):
        # Send a GET request to mark-as-read, which should not be allowed
        response = self.client.get(reverse("mark-as-read", args=[self.notification1.id]))
        
        # Check the response status code and JSON content
        self.assertEqual(response.status_code, 405)
        self.assertJSONEqual(response.content, {"status": "error", "message": "Invalid request method."})

    def test_mark_all_notifications_as_read_success(self):
        # Send a POST request to mark all notifications as read
        response = self.client.post(reverse("mark-all-as-read"))
        
        # Check the response status code and JSON content
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "success", "updated_count": 2})
        
        # Verify that all notifications are marked as read in the database
        self.notification1.refresh_from_db()
        self.notification2.refresh_from_db()
        self.assertTrue(self.notification1.is_read)
        self.assertTrue(self.notification2.is_read)

    def test_mark_all_notifications_as_read_invalid_method(self):
        # Send a GET request to mark-all-as-read, which should not be allowed
        response = self.client.get(reverse("mark-all-as-read"))
        
        # Check the response status code and JSON content
        self.assertEqual(response.status_code, 405)
        self.assertJSONEqual(response.content, {"status": "error", "message": "Invalid request method."})

    def test_delete_notification_success(self):
        # Send a POST request to delete the notification
        response = self.client.post(reverse("delete-notification", args=[self.notification1.id]))
        
        # Check the response status code and JSON content
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "success", "message": "Notification deleted successfully."})
        
        # Verify the notification no longer exists in the database
        self.assertFalse(Notification.objects.filter(id=self.notification1.id).exists())

    def test_delete_notification_invalid_method(self):
        # Send a GET request (instead of POST) to delete the notification
        response = self.client.get(reverse("delete-notification", args=[self.notification1.id]))
        
        # Check for the 405 response status code
        self.assertEqual(response.status_code, 405)
        self.assertJSONEqual(response.content, {"status": "error", "message": "Invalid request method."})
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Notification
from .utils import send_notification
from .models import Notification

class NotificationTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(username="testuser", password="password123")

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

class NotificationModelTest(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(username='testuser', password='12345')

    def test_notification_creation(self):
        notification = Notification.objects.create(
            user=self.user,
            message='New notification message',
        )
        self.assertEqual(str(notification), f"Notification for {self.user.username}: New notification message")
        self.assertFalse(notification.is_read)
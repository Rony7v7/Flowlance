from django.test import TestCase
from django.contrib.auth.models import User
from .models import Notification
from .utils import send_notification  # Adjust the import path to your `send_notification` function
from channels.testing import ChannelsLiveServerTestCase
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class NotificationTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(username="testuser", password="password123")

    def test_notification_creation(self):
        # Call the send_notification function
        notification_message = "Test notification message"
        send_notification(notification_message, self.user)

        # Verify that a Notification object was created for the user
        notification_exists = Notification.objects.filter(user=self.user, message=notification_message).exists()
        self.assertTrue(notification_exists)

    def test_notification_message_content(self):
        # Test if the created notification has the correct message content
        notification_message = "Test message for content verification"
        send_notification(notification_message, self.user)

        notification = Notification.objects.get(user=self.user, message=notification_message)
        self.assertEqual(notification.message, notification_message)

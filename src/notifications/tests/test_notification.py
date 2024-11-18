from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from profile.models import FreelancerProfile, ProfileConfiguration
from ..models import Notification
from django.utils.translation import gettext as _

class NotificationViewTest(TestCase):
    def setUp(self):
        # Crear usuario
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Crear configuración de perfil
        self.profile_config = ProfileConfiguration.objects.create(
            notification_when_profile_visited=True,
            sending_notification_to_email=False,
            periodicity_of_notification_report='D',
            silent_start='22:00',
            silent_end='06:00',
            receive_project_updates=True,
            receive_messages=True,
            receive_job_opportunities=True,
        )

        # Crear perfil de freelancer
        self.freelancer_profile = FreelancerProfile.objects.create(
            user=self.user,
            full_name="John Doe",
            identification="1234567890",
            phone="123456789",
            job_title="Developer",
            profileconfiguration=self.profile_config
        )

        # Crear notificación
        self.notification1 = Notification.objects.create(
            user=self.user,
            title="Test Notification",
            notification_type="PY",
            is_read=False
        )

        # Iniciar sesión
        self.client.login(username='testuser', password='12345')

    def test_notifications_list(self):
        response = self.client.get(reverse('notifications'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Notification")
        self.assertEqual(response.context['notifications'].count(), 1)

    def test_filter_notifications_by_type(self):
        Notification.objects.create(
        user=self.user,
        title="Another Notification",
        notification_type="MSG",
        is_read=False,
        )
        response = self.client.get(reverse('notifications') + '?filter=PY')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Notification")
        self.assertNotContains(response, "Another Notification")


    def test_filter_notifications_no_results(self):
        response = self.client.get(reverse('notifications') + '?filter=OTH')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['notifications']), 0)


    def test_delete_notification(self):
        """Test deleting a notification."""
        response = self.client.post(reverse('delete-notification', args=[self.notification1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Notification.objects.filter(id=self.notification1.id).exists())

    def test_mark_all_notifications_as_read(self):
        """Test marking all notifications as read."""
        response = self.client.post(reverse('mark-all-as-read'))
        self.assertEqual(response.status_code, 302)  # Redirect expected
        notifications = Notification.objects.filter(user=self.user)
        self.assertTrue(all(notification.is_read for notification in notifications))

    def test_search_notifications(self):
        """Test searching notifications by query."""
        response = self.client.get(reverse('notifications') + '?q=Test')
        self.assertEqual(response.status_code, 200)
        notifications = response.context['notifications']
        self.assertEqual(len(notifications), 1)
        self.assertEqual(notifications[0].title, "Test Notification")
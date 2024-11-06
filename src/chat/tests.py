from django.test import TestCase
from django.contrib.auth.models import User
from project.models import Project, ProjectMember
from chat.models import ChatRoom, Message
from django.urls import reverse
from channels.testing import WebsocketCommunicator
from chat.consumers import ChatConsumer
from asgiref.testing import ApplicationCommunicator
import json

class ChatModelsTestCase(TestCase):
    def setUp(self):
        # Crear usuarios y proyecto para las pruebas
        self.user1 = User.objects.create_user(username="user1", password="pass")
        self.user2 = User.objects.create_user(username="user2", password="pass")
        self.project = Project.objects.create(title="Test Project")

    def test_chat_room_creation(self):
        # Crear una sala de chat
        room = ChatRoom.objects.create(project=self.project, name="room1")
        self.assertEqual(room.project, self.project)
        self.assertEqual(room.name, "room1")

    def test_message_creation(self):
        # Crear un mensaje y verificar que se guarda correctamente
        message = Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            project=self.project,
            content="Hello"
        )
        self.assertEqual(message.sender, self.user1)
        self.assertEqual(message.recipient, self.user2)
        self.assertEqual(message.content, "Hello")

    def test_soft_delete(self):
        # Verificar que el soft delete funcione
        message = Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            project=self.project,
            content="To be deleted"
        )
        message.hidden_for_sender = True
        message.hidden_for_recipient = True
        message.save()

        # Verificar que los flags de soft delete están establecidos correctamente
        self.assertTrue(message.hidden_for_sender)
        self.assertTrue(message.hidden_for_recipient)



class ChatViewsTestCase(TestCase):
    def setUp(self):
        # Configuración de datos de prueba
        self.user1 = User.objects.create_user(username="user1", password="pass")
        self.user2 = User.objects.create_user(username="user2", password="pass")
        self.project = Project.objects.create(title="Test Project")
        ProjectMember.objects.create(user=self.user1, project=self.project)
        ProjectMember.objects.create(user=self.user2, project=self.project)
        self.client.login(username="user1", password="pass")

    def test_chat_room_view(self):
        url = reverse("chat_room", args=[self.project.id, self.user2.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chat con user2")

    def test_soft_delete_chat(self):
        # Crear un mensaje y luego eliminarlo para un usuario
        message = Message.objects.create(
            sender=self.user1,
            recipient=self.user2,
            project=self.project,
            content="Hello"
        )
        url = reverse("soft_delete_chat", args=[self.project.id, self.user2.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

        # Recargar el mensaje y verificar que está oculto para el usuario
        message.refresh_from_db()
        self.assertTrue(message.hidden_for_sender)

    def test_upload_file_view(self):
        # Probar la subida de archivos en el chat
        url = reverse("upload_file")
        with open("test_file.txt", "w") as f:
            f.write("File content")
        with open("test_file.txt", "rb") as f:
            response = self.client.post(url, {"file": f})
            self.assertEqual(response.status_code, 200)
            self.assertIn("filename", response.json())


class ChatConsumerTestCase(TestCase):
    async def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="pass")
        self.user2 = User.objects.create_user(username="user2", password="pass")
        self.project = Project.objects.create(title="Test Project")

    async def test_send_message(self):
        communicator = WebsocketCommunicator(
            ChatConsumer.as_asgi(),
            f"/ws/chat/{self.project.id}_{self.user2.id}/"
        )
        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        # Enviar un mensaje
        await communicator.send_json_to({
            "message": "Hello",
            "sender_id": self.user1.id,
            "recipient_id": self.user2.id,
            "project_id": self.project.id
        })

        # Recibir el mensaje en el WebSocket
        response = await communicator.receive_json_from()
        self.assertEqual(response["message"], "Hello")
        self.assertEqual(response["user"], self.user1.username)

        await communicator.disconnect()

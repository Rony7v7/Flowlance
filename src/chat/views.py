from django.shortcuts import redirect, render, get_object_or_404
from project.models import Project, ProjectMember
from .models import ChatRoom


def chat_overview(request):
    projects = Project.objects.filter(memberships__user=request.user)
    return render(request, 'chat/chat_overview.html', {'projects': projects})

from .models import ChatRoom, Message

def chat_room(request, project_id, member_id):
    project = get_object_or_404(Project, id=project_id)
    member = get_object_or_404(ProjectMember, id=member_id, project=project)
    room_name = f"{project_id}_{member_id}"

    # Crear sala de chat si no existe
    room, created = ChatRoom.objects.get_or_create(project=project, name=room_name)

    # Cargar el historial de mensajes
    messages = Message.objects.filter(project=project, sender=request.user, recipient=member.user).order_by("timestamp")

    return render(request, 'chat/chat_room.html', {
        'room_name': room_name,
        'project': project,
        'member': member.user,
        'messages': messages  # Pasar los mensajes al template
    })


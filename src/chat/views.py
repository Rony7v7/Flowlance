from django.shortcuts import redirect, render, get_object_or_404
from project.models import Project, ProjectMember
from .models import ChatRoom
from .models import ChatRoom, Message

def chat_overview(request):
    projects = Project.objects.filter(memberships__user=request.user)
    return render(request, 'chat/chat_overview.html', {'projects': projects})



# views.py
from django.shortcuts import redirect, render, get_object_or_404
from project.models import Project, ProjectMember
from .models import ChatRoom, Message

def chat_room(request, project_id, member_id):
    project = get_object_or_404(Project, id=project_id)
    member = get_object_or_404(ProjectMember, id=member_id, project=project)  # Member es el recipiente del mensaje
    room_name = f"{project_id}_{min(request.user.id, member.user.id)}_{max(request.user.id, member.user.id)}"

    # Crear sala de chat si no existe
    room, created = ChatRoom.objects.get_or_create(project=project, name=room_name)

    # Cargar el historial de mensajes para ambos usuarios en este proyecto
    messages = Message.objects.filter(
        project=project,
        sender__in=[request.user, member.user],
        recipient__in=[request.user, member.user]
    ).order_by("timestamp")

    return render(request, 'chat/chat_room.html', {
        'room_name': room_name,
        'project': project,
        'member': member.user,
        'messages': messages  # Pasar los mensajes al template
    })



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

from django.db.models import Q

def chat_room(request, project_id, member_id):
    project = get_object_or_404(Project, id=project_id)
    member = get_object_or_404(ProjectMember, id=member_id, project=project)
    room_name = f"{project_id}_{member_id}"

    # Create chat room if it doesn't exist
    room, created = ChatRoom.objects.get_or_create(project=project, name=room_name)

    # Load message history for both sender and recipient
    messages = Message.objects.filter(
        Q(project=project, sender=request.user, recipient=member.user) |
        Q(project=project, sender=member.user, recipient=request.user)
    ).order_by("timestamp")

    # Get all projects for the sidebar
    projects = Project.objects.filter(memberships__user=request.user)

    return render(request, 'chat/chat_room.html', {
        'room_name': room_name,
        'project': project,
        'member': member.user,
        'messages': messages,
        'projects': projects,
        'current_member': member.user,
    })


# views.py

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q

@require_POST
def delete_chat(request, project_id, member_id):
    # Obtener el proyecto y el miembro correspondiente
    project = get_object_or_404(Project, id=project_id)
    member = get_object_or_404(ProjectMember, id=member_id, project=project)

    # Filtrar los mensajes en ambas direcciones (enviados y recibidos)
    Message.objects.filter(
        Q(project=project) & (
            Q(sender=request.user, recipient=member.user) |
            Q(sender=member.user, recipient=request.user)
        )
    ).delete()

    return JsonResponse({'status': 'success'})




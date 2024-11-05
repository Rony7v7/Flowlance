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

# views.py

from django.db.models import Q

def chat_room(request, project_id, member_id):
    project = get_object_or_404(Project, id=project_id)
    member = get_object_or_404(ProjectMember, id=member_id, project=project)
    room_name = f"{project_id}_{member_id}"
    
    # Crear o obtener la sala de chat
    room, created = ChatRoom.objects.get_or_create(project=project, name=room_name)
    
    # Filtrar mensajes de acuerdo con el usuario que hace la solicitud
    if request.user == member.user:
        messages = Message.objects.filter(
            Q(project=project, sender=request.user, recipient=member.user, hidden_for_sender=False) |
            Q(project=project, sender=member.user, recipient=request.user, hidden_for_recipient=False)
        ).order_by("timestamp")
    else:
        messages = Message.objects.filter(
            Q(project=project, sender=request.user, recipient=member.user, hidden_for_sender=False) |
            Q(project=project, sender=member.user, recipient=request.user, hidden_for_recipient=False)
        ).order_by("timestamp")
    
    # Cargar los proyectos en los que está el usuario para la barra lateral
    projects = Project.objects.filter(memberships__user=request.user)

    return render(request, 'chat/chat_room.html', {
        'room_name': room_name,
        'project': project,
        'member': member.user,
        'messages': messages,
        'projects': projects,
        'current_member': member.user,
    })




from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def soft_delete_chat(request, project_id, member_id):
    project = get_object_or_404(Project, id=project_id)
    member = get_object_or_404(ProjectMember, id=member_id, project=project)


    if request.user == member.user:
        Message.objects.filter(
            Q(project=project, sender=request.user, recipient=member.user) |
            Q(project=project, sender=member.user, recipient=request.user)
        ).update(hidden_for_recipient=True)
    else:
        Message.objects.filter(
            Q(project=project, sender=request.user, recipient=member.user) |
            Q(project=project, sender=member.user, recipient=request.user)
        ).update(hidden_for_sender=True)

    return JsonResponse({'status': 'success'})



# views.py

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q

@require_POST
def delete_chat(request, project_id, member_id):
    # Obtener el proyecto y el miembro correspondiente
    project = get_object_or_404(Project, id=project_id)
    member = get_object_or_404(ProjectMember, id=member_id, project=project)


    Message.objects.filter(
        Q(project=project) & (
            Q(sender=request.user, recipient=member.user) |
            Q(sender=member.user, recipient=request.user)
        )
    ).delete()

    return JsonResponse({'status': 'success'})



# views.py
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Message
from django.core.files.storage import default_storage
from django.conf import settings
from django.contrib.auth.models import User

@require_POST
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        project_id = request.POST.get('project_id')
        sender_id = request.POST.get('sender_id')
        recipient_id = request.POST.get('recipient_id')
        message_text = request.POST.get('message', '')

        sender = User.objects.get(id=sender_id)
        recipient = User.objects.get(id=recipient_id)
        project = Project.objects.get(id=project_id)

        message = Message.objects.create(
            sender=sender,
            recipient=recipient,
            project=project,
            content=message_text,
            file=file
        )


        return JsonResponse({
            'user': sender.username,
            'message': message_text,
            'file_url': message.file.url if message.file else None
        })


from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.files.storage import default_storage

@require_POST
def upload_message(request):
    project_id = request.POST.get('project_id')
    sender_id = request.POST.get('sender_id')
    recipient_id = request.POST.get('recipient_id')
    message_content = request.POST.get('message', '')
    file = request.FILES.get('file')  

    sender = User.objects.get(id=sender_id)
    recipient = User.objects.get(id=recipient_id)
    project = Project.objects.get(id=project_id)


    message = Message.objects.create(
        sender=sender,
        recipient=recipient,
        project=project,
        content=message_content,
        file=file if file else None
    )

    return JsonResponse({
        'status': 'success',
        'user': sender.username,
        'message': message.content,
        'file': message.file.url if message.file else None,
        'filename': message.file.name if message.file else None
    })

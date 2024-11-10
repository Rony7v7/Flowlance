from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from project.forms import EventForm
from ..models import Event


@login_required
def all_events(request):
    project_id = request.GET.get('project_id')
    
    try:
        project_id = int(project_id)  
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid project ID'}, status=400)
    
    if project_id:
        all_events = Event.objects.filter(project_id=project_id)
    else:
        all_events = Event.objects.none()

    events = []
    for event in all_events:
        events.append({
            'title': event.name,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),
        })
    return JsonResponse(events, safe=False)


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)

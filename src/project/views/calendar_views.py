from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ..models import Events
import json

def all_events(request):
    project_id = request.GET.get('project_id')
    
    try:
        project_id = int(project_id)  
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid project ID'}, status=400)
    
    if project_id:
        all_events = Events.objects.filter(project_id=project_id)
    else:
        all_events = Events.objects.none()

    events = []
    for event in all_events:
        events.append({
            'title': event.name,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),
        })
    return JsonResponse(events, safe=False)

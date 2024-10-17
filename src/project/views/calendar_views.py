from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ..models import Events
import json


def all_events(request):
    all_events = Events.objects.all()
    events = []
    for event in all_events:
        events.append({
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),    
        })
    return JsonResponse(events, safe=False)
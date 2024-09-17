from django.shortcuts import render

# Create your views here.

def notifications(request):
    return render(request, "navigation/building.html")
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

building = "dashboard/building.html"

@login_required
def home(request):
    return render(request, building)

@login_required
def projects(request):
    return render(request, building)

@login_required
def chat(request):
    return render(request, building)

@login_required
def profile(request):
    return render(request, building)

@login_required
def settings(request):
    return render(request, building)

@login_required
def notifications(request):
    return render(request, building)
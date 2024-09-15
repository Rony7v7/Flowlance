from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Archivo HTML base
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
def create_profile(request):
    return render(request, 'dashboard/create_profile.html')


@login_required
def settings(request):
    return render(request, building)

@login_required
def notifications(request):
    return render(request, building)

@login_required
def dashboard(request):
    return render(request, building)

@login_required
def support(request):
    return render(request, building)

@login_required
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return render(request, building)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Archivo HTML base
building = "dashboard/building.html"

@login_required
def dashboard(request):
    return render(request, building)


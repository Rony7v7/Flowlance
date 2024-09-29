from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from ..forms import FreelancerRegisterForm, CompanyRegisterForm
from django.db import IntegrityError


def register_freelancer(request):
    if request.method == 'POST':
        form = FreelancerRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            # try:
                user = form.save()
                login(request, user)
                # messages.success(request, 'Registro de Freelancer exitoso.')
                return redirect("/dashboard/")
            # except IntegrityError:
                # El error ya ha sido capturado y manejado en el formulario, solo muestra mensaje
                # messages.error(request, "Error al crear el perfil: revisa los campos.")
        # else:
            # messages.error(request, "Error en el formulario. Por favor revisa los campos.")
    else:
        form = FreelancerRegisterForm()
    return render(request, 'profile/register_freelancer.html', {'form': form})



def register_company(request):
    if request.method == 'POST':
        form = CompanyRegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, 'Registro de Empresa exitoso.')
                return redirect("/dashboard/")
            except IntegrityError:
                # El error ya ha sido capturado y manejado en el formulario, solo muestra mensaje
                messages.error(request, "Error al crear el perfil: revisa los campos.")
        else:
            messages.error(request, "Error en el formulario. Por favor revisa los campos.")
    else:
        form = CompanyRegisterForm()
    return render(request, 'profile/register_company.html', {'form': form})

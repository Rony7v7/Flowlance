from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..forms import FreelancerRegisterForm, CompanyRegisterForm
from django.db import IntegrityError



def register_freelancer(request):
    if request.method == 'POST':
        form = FreelancerRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'profile/register_freelancer.html', {'form': form, 'registration_successful': True})

    else:
        form = FreelancerRegisterForm()
    return render(request, 'profile/register_freelancer.html', {'form': form})



def register_company(request):
    registration_successful = False
    if request.method == 'POST':
        form = CompanyRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                registration_successful = True
                # No renderices el formulario nuevamente si el registro es exitoso
                return render(request, 'profile/register_company.html', {
                    'form': CompanyRegisterForm(),  # Limpia el formulario
                    'registration_successful': registration_successful
                })
            except IntegrityError:
                form.add_error(None, 'Error al crear el usuario, por favor intenta de nuevo.')
    else:
        form = CompanyRegisterForm()
    
    return render(request, 'profile/register_company.html', {
        'form': form,
        'registration_successful': registration_successful
    })

from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..forms import FreelancerRegisterForm, CompanyRegisterForm


def register_freelancer(request):
    if request.method == 'POST':
        form = FreelancerRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/dashboard/")

    else:
        form = FreelancerRegisterForm()
    return render(request, 'profile/register_freelancer.html', {'form': form})



def register_company(request):
    if request.method == 'POST':
        form = CompanyRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/dashboard/")
    else:
        form = CompanyRegisterForm()
    return render(request, 'profile/register_company.html', {'form': form})

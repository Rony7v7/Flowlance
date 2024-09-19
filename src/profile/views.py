from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddSkillsForm, AddWorkExperienceForm, UploadCVForm
from .models import FreelancerProfile, CurriculumVitae, Portfolio, FreelancerProfile
from .forms import AddProjectForm, AddCourseForm

@login_required
def add_course(request):
    profile = FreelancerProfile.objects.get(user=request.user)
    
    portfolio, created = Portfolio.objects.get_or_create(freelancer_profile=profile)

    if request.method == 'POST':
        form = AddCourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.portfolio = portfolio  
            course.save()
            return redirect('freelancer_profile')  
    else:
        form = AddCourseForm()

    return render(request, 'profile/add_course.html', {'form': form})


@login_required
def add_project(request):
    profile = FreelancerProfile.objects.get(user=request.user)
    
    portfolio, created = Portfolio.objects.get_or_create(freelancer_profile=profile)

    if request.method == 'POST':
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = portfolio  
            project.save()
            return redirect('freelancer_profile')  
    else:
        form = AddProjectForm()

    return render(request, 'profile/add_project.html', {'form': form})


@login_required
def upload_curriculum(request):
    profile = FreelancerProfile.objects.get(user=request.user)
    try:
        curriculum = profile.freelancer_cv  
    except CurriculumVitae.DoesNotExist:
        curriculum = None  

    if request.method == 'POST':
        form = UploadCVForm(request.POST, request.FILES, instance=curriculum)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.profile = profile  
            cv.save()
            return redirect('freelancer_profile')
    else:
        form = UploadCVForm(instance=curriculum)

    return render(request, 'profile/upload_curriculum.html', {'form': form})


@login_required
def freelancer_profile(request, username=None):
    if username is None:
        profile = FreelancerProfile.objects.get(user=request.user)
    else:
        profile = get_object_or_404(FreelancerProfile, user__username=username)

    try:
        portfolio = profile.portfolio_profile
        projects = portfolio.projects.all()
        courses = portfolio.courses.all()
    except Portfolio.DoesNotExist:
        portfolio = None
        projects = None
        courses = None

    context = {
        'profile': profile,
        'skills': profile.skills.all(),
        'experiences': profile.freelancer_work_experience.all(),
        'portfolio': portfolio,
        'projects': projects,
        'courses': courses,
    }

    return render(request, 'profile/freelancer_profile.html', context)




@login_required
def add_skills(request):
    user = request.user  
    
    if request.method == 'POST':
        form = AddSkillsForm(request.POST, user=user)  
        if form.is_valid():
            form.save(user=user)  
        return redirect('freelancer_profile')
    else:
        form = AddSkillsForm(user=user)

    return render(request, 'profile/add_skills.html', {'form': form})

@login_required
def add_experience(request):
    user = request.user
    
    if request.method == 'POST':
        form = AddWorkExperienceForm(request.POST)
        if form.is_valid():
            form.save(user=user)  
            return redirect('freelancer_profile')  
    else:
        form = AddWorkExperienceForm()

    return render(request, 'profile/add_experience.html', {'form': form})


# @login_required
# def calificar_freelancer(request, username):
#     # Obtener el usuario freelancer basado en el username
#     freelancer = get_object_or_404(User, username=username)
    
#     if request.method == 'POST':
#         # Obtener los datos del formulario
#         estrellas = request.POST.get('estrellas')
#         comentario = request.POST.get('descripcion')

#         # Crear una nueva instancia de calificación
#         nueva_calificacion = Calificacion(
#             freelancer=freelancer,  # Freelancer a quien se califica
#             usuario=request.user,  # Usuario que hace la calificación
#             estrellas=estrellas,  # Número de estrellas
#             comentario=comentario  # Comentario opcional
#         )
#         nueva_calificacion.save()

#         # Mensaje de éxito o redirigir al perfil del freelancer
#         return redirect('freelancer_profile', username=freelancer.username)

#     return render(request, 'profile/calification.html', {'freelancer': freelancer})


















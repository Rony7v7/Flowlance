from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required
def settings(request):
    return render(request, "settings/account_settings.html")

@login_required
def security_settings(request):
    user = request.user
    profile, profile_type = user.get_profile_info()  # Use the get_profile_info method
    # Check if profile exists and handle the case when it's None
    if profile:
        has_2FA_on = profile.has_2FA_on
    else:
        has_2FA_on = False  # Default value if no profile is found

    return render(request, "settings/security_settings.html", {"has_2FA_on": has_2FA_on})


@login_required
def toggle_2fa(request):
    user = request.user
    profile, profile_type = user.get_profile_info()  # Use the get_profile_info method

    if request.method == 'POST':
        has_2FA_on = request.POST.get('has_2FA_on') == 'on'
        if profile:  # If the user has a profile (either Freelancer or Company)
            profile.has_2FA_on = has_2FA_on
            profile.save()

        return redirect('security_settings')  # Redirect to the profile page or another relevant page


@login_required
def toggle_notification_when_profile_visited(request):
    user = request.user
    profile, profile_type = user.get_profile_info()  # Use the get_profile_info method

    if request.method == 'POST':
        notification_when_profile_visited_variable = request.POST.get('notification_when_profile_visited_variable') == 'on' #esto se lo deberias pasar desde la form, para ver si lo quiere activar o no
        if profile:  # If the user has a profile (either Freelancer or Company)
            profile.profileconfiguration.notification_when_profile_visited = notification_when_profile_visited_variable
            profile.profileconfiguration.save()

        return redirect('security_settings')  # Redirect to the profile page or another relevant page

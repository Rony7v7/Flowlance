from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        print("Adaptador personalizado activado")  # Este print verifica si el adaptador funciona
        user = super().save_user(request, sociallogin, form)
        if sociallogin.account.provider == 'google':
            email = sociallogin.account.extra_data.get('email')
            print("Correo obtenido de Google:", email)  # Debugging
            request.session['google_email'] = email  # Guardar el correo en la sesión
            print("Correo guardado en sesión:", request.session['google_email'])  # Confirmación
            print("Correo guardado en sesión (adaptador):", request.session.get('google_email'))
        return user

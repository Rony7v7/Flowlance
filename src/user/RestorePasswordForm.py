from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext as _

class StyledPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'class': 'my-4 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-primary_medium focus:border-primary_medium sm:text-sm',
            'placeholder': _('Contraseña actual')
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'my-4 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-primary_medium focus:border-primary_medium sm:text-sm',
            'placeholder': _('Nueva contraseña')
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'my-4 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-primary_medium focus:border-primary_medium sm:text-sm',
            'placeholder': _('Confirmar nueva contraseña')
        })

        # Setting labels in Spanish
        self.fields['old_password'].label = _('Contraseña actual')
        self.fields['new_password1'].label = _('Nueva contraseña')
        self.fields['new_password2'].label = _('Confirmar nueva contraseña')

        # Optional: Help texts can also be set in Spanish if desired
        self.fields['old_password'].help_text = _('Introduce tu contraseña actual.')
        self.fields['new_password1'].help_text = _('La nueva contraseña debe tener al menos 8 caracteres.')
        self.fields['new_password2'].help_text = _('Introduce la misma contraseña que antes para confirmarla.')

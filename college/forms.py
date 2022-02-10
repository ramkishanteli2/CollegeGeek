from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import authenticate,get_user_model,password_validation
        
class SetNewPassword(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'),widget=forms.PasswordInput(attrs={'class':'form-control','autofocus':True}),strip=False)
    new_password1 = forms.CharField(label=_('New Password'),widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password'}),strip=False,help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New Password'),widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password'}),strip=False)

class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email','class':'form-control'})
    )

class SetNewPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
    )
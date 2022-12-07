from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm,
    PasswordResetForm, SetPasswordForm)
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from Core.auth_forms import AuthForm
from users.models import User


class EmailUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class EmailUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)


class SignupForm(forms.ModelForm, AuthForm):
    confirm_password = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = ({
            'password': forms.PasswordInput()
        })

    def clean(self):
        cleaned_data = super().clean()
        if (cleaned_data.get('password')
                != cleaned_data.get('confirm_password')):
            self.add_error('confirm_password', 'Пароли не совпадают')


class UpdateUserForm(forms.ModelForm, AuthForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'birthday')
        widgets = ({
            'birthday': forms.DateInput(attrs={'type': 'date'})
        })


class BootstrapLoginForm(AuthenticationForm, AuthForm):
    pass


class BootstrapPasswordChangeForm(PasswordChangeForm, AuthForm):
    pass


class BoostrapPasswordResetForm(PasswordResetForm, AuthForm):
    pass


class BootstrapPasswordResetConfirmForm(SetPasswordForm, AuthForm):
    pass

from django import forms
from django.contrib.auth import authenticate, get_user_model, login


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
    )

    class Meta:
        # We retrieve the user model dynamically by using the get_user_model() function provided by the auth application.
        model = get_user_model()
        fields = ['username', 'first_name', 'email']

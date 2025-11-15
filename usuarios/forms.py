from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
        "placeholder": "Ingresa tu contraseña"
    }))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={
        "class": "input",
        "placeholder": "Repite tu contraseña"
    }))

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("password2"):
            raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input"}))

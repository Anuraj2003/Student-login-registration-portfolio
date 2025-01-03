from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ap6.models import StudentProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields=['bio']
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields ='__all__'
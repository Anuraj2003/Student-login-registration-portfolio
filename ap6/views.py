from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ap6.Forms import  RegistrationForm, ProfileForm
from ap6.Forms import RegistrationForm,UpdateProfileForm
from ap6.models import StudentProfile
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        form = RegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {'form': form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')
def update_profile(request):
    profile, created = StudentProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('dashboard')
    else:
        form = UpdateProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
# Create your views here.

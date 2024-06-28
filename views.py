from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import CustomUser, UserProfile, LoginTable
import logging

logger = logging.getLogger(__name__)

def home_view(request):
    return render(request, 'authentication/home.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                UserProfile.objects.create(
                    user=user,
                    email=user.email,
                    password=form.cleaned_data["password1"],
                    cpassword=form.cleaned_data["password2"]
                )
                LoginTable.objects.create(
                    username=user.username,
                    password=form.cleaned_data["password1"],
                    cpassword=form.cleaned_data["password2"],
                    user_type=user.user_type
                )
                messages.success(request, 'Registration successful.')
                return redirect('login')
            except Exception as e:
                logger.error(f"Error saving user: {e}")
                messages.error(request, 'Registration failed. Please try again later.')
        else:
            logger.error(f"Form is not valid: {form.errors}")
            messages.error(request, 'Invalid form data. Please correct the errors.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'authentication/register.html', {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if hasattr(user, 'user_type'):
                if user.user_type == 'admin':
                    return redirect('admin_dashboard')
                elif user.user_type == 'doctor':
                    return redirect('doctor_dashboard')
                elif user.user_type == 'user':
                    return redirect('patient_dashboard')
                else:
                    messages.info(request, 'User type not defined.')
            else:
                messages.info(request, 'User type attribute is missing.')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'authentication/login.html')
def admin_view(request):
    if request.user.is_authenticated and request.user.user_type == 'admin':
        return render(request, 'authentication/admin_dashboard.html', {'username': request.user.username})
    else:
        return redirect('login')

def patient_view(request):
    if request.user.is_authenticated and request.user.user_type == 'user':
        return render(request, 'authentication/patient_dashboard.html', {'username': request.user.username})
    else:
        return redirect('login')

def doctor_view(request):
    if request.user.is_authenticated and request.user.user_type == 'doctor':
        return render(request, 'authentication/doctor_dashboard.html', {'username': request.user.username})
    else:
        return redirect('login')

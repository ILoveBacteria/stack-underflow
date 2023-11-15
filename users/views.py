from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse

from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from users.models import User


# Create your views here.
def user_register_view(request):
    if request.method == 'GET':
        form = UserRegisterForm()
        return render(request, 'user/user_register_form.html', {'form': form})
    form = UserRegisterForm(request.POST)
    if not form.is_valid():
        messages.warning(request, 'register unsuccessfully')
        return render(request, 'user/user_register_form.html', {'form': form})
    user = form.save()
    messages.success(request, 'you registered successfully')
    login(request, user)
    return redirect('users:home')
    


def user_login_view(request):
    pass


def user_logout_view(request):
    pass


def user_profile_view(request, uid):
    pass


def user_profile_edit_view(request):
    pass


def user_home_view(request):
    return render(request, 'home.html')

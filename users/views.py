from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, 'user/user_login_form.html', {'form': form})
    form = UserLoginForm(request.POST)
    if form.is_valid():
        user = authenticate(request, username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            messages.success(request, 'login successful')
            return redirect('users:home')
    messages.warning(request, 'login unsuccessful')
    return render(request, 'user/user_login_form.html', {'form': form})


def user_logout_view(request):
    logout(request)
    return redirect('users:home')


def user_profile_view(request, uid):
    user = get_object_or_404(User, pk=uid)
    return render(request, 'user/user_profile_view.html', {'user': user})


def user_profile_edit_view(request):
    if request.method == 'GET':
        form = UserUpdateForm(instance=request.user)
        return render(request, 'user/user_edit.html', {'form': form})


def user_home_view(request):
    return render(request, 'home.html')

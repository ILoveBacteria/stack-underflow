from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login

from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from users.models import User


# Create your views here.
def user_register_view(request):
    pass


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

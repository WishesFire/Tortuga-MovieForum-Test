from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.backends import BaseBackend
from .models import Profile
from users.email import create_email_message
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View


def register_user(request, *args, **kwargs):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = False
            new_user.set_password(form.cleaned_data['password1'])
            Profile.objects.create(user=new_user)
            new_user.save()

            create_email_message(request, form.cleaned_data['email'], new_user)
            messages.info(request, 'Активируйте свой аккаунт')

            return redirect('main-page')
        else:
            messages.error(request, 'Ошибка')
    else:
        form = RegistrationForm()

    return render(request, 'users/registration.html', {'form': form})


def login_user(request, *args, **kwargs):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user and user.is_active:
                login(request, user)
                if not cd['remember']:
                    request.session.set_expiry(0)
                return redirect('main-page')
            else:
                messages.error(request, 'Ошибка')
        else:
            messages.error(request, 'Ошибка')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        user = User.objects.get(email=username)
        if user is not None:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExists:
            return None


class EditProfile(View):
    @login_required
    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'users/dashboard.html', {'user_form': user_form, 'profile_form': profile_form})

    @login_required
    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return render(request, 'users/dashboard.html', {'user_form': user_form, 'profile_form': profile_form})
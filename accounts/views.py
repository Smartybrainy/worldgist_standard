from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Oops! Username already taken!')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Oops! Email already taken!')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                                username=username, email=email,
                                                password=password)
                user.save()
                messages.info(request, f"{user} registered successfully")
                return redirect('accounts:login')
            return redirect('accounts:register')

        else:
            messages.info(request, 'Oops! Password does not match!')
            return redirect('accounts:register')
    else:
        return render(request, 'main/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(
                request, f'Successfully signed in as {user}')
            return redirect("/")
        else:
            messages.warning(request, 'Oops! Invalid credentail !')
            return redirect('accounts:login')
    else:
        return render(request, 'main/login.html')


def remember_user(request, template_name="main/login.html",
                  extra_context=None):
    response = auth_views.login(request, template_name)
    if request.POST.has_key('remember_me'):
        request.sessions.set_expiry(2419200)  # 4weeks in seconds


def logout(request):
    user = request.user
    auth.logout(request)
    messages.success(
        request, f'{user} Have a nice day.')
    return redirect('/')


class Profile(ListView):
    model = Profile
    template_name = 'accounts/user_profile.html'


@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None,
                                   request.FILES or None,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('accounts:profile-view')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/user_profile.html', context)


def why_sign_up(request):
    return render(request, 'accounts/why_sign_up.html')

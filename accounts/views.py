from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import views as auth_views
from django.contrib import messages


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
            return redirect("/")
        else:
            messages.error(request, 'Oops! Invalid credentail !')
            return redirect('accounts:login')
    else:
        return render(request, 'main/login.html')


def remember_user(request, template_name="main/login.html",
                  extra_context=None):
    response = auth_views.login(request, template_name)
    if request.POST.has_key('remember_me'):
        request.sessions.set_expiry(1209600)  # weeks


def logout(request):
    auth.logout(request)
    return redirect('/')

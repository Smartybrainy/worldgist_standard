from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('remember_me/', views.remember_user, {'template_name': 'main/login.html'},
         name="remember-me"),
    path('profile/', views.Profile.as_view(), name="profile"),
    path('profile_view/', views.profile_view, name='profile-view'),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = "accounts"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('why-sign-up/', views.why_sign_up, name="why-sign-up"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

    path('remember_me/', views.remember_user, {'template_name': 'main/login.html'},
         name="remember-me"),

    path('profile/', views.Profile.as_view(), name="profile"),
    path('profile_view/', views.profile_view, name='profile-view'),

    # For reset password
    path('reset_password/', auth_views.PasswordResetView.as_view(
         template_name="registration/password_reset.html"
         ),
         name="password_reset"),
    path('reset-password_/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="registration/password_reset_done.html"
         ),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="registration/password_reset_confirm.html"
         ),
         name="password_reset_comfirm"),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="registration/password_reset_complete.html"
         ),
         name="password_reset_complete"),
]

from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    username = forms.CharField(required=False)

    class Meta:
        model = User
        help_texts = {'username': None}
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    gender = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['gender', 'image']

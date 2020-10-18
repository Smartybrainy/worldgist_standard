from django.shortcuts import render, redirect
from django.views.generic import TemplateView


def not_ready(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    return render(request, "agent/not_ready.html")


class SignUpFirst(TemplateView):
    template_name = "agent/sign_up_first.html"

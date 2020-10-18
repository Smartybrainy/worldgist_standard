from django.urls import path
from .views import not_ready, SignUpFirst

app_name = "agent"


urlpatterns = [
    path('agent/', not_ready, name="not-ready"),
    path('sign-up-first/', SignUpFirst.as_view(), name="sign-up-first")
]

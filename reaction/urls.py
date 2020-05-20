from django.urls import path
from . import views

app_name = "reaction"

urlpatterns = [
    path('', views.ReactionList.as_view(), name="reaction-list"),
    path('add_reaction/',  views.add_reaction, name="add-reaction"),
]

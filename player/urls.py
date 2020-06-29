from django.urls import path
from .import views

app_name = 'player'

urlpatterns = [
    path('video/', views.VideoList.as_view(), name="video-list"),
    path('audio/', views.MusicList.as_view(), name="audio-list")
]

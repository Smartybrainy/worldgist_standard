from django.urls import path
from .import views

app_name = 'player'

urlpatterns = [
    path('video/', views.VideoList.as_view(), name="video-list"),
    path('video/popular/', views.popular_video, name="popular-video"),
    path('<pk>/video_detail/',
         views.VideoDetail.as_view(), name="video-detail"),
    path('audio/', views.MusicList.as_view(), name="audio-list"),
    path('<pk>/audio_detail/', views.MusicDetail.as_view(), name="audio-detail")
]

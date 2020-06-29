from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Video, Music


class VideoList(ListView):
    model = Video
    template_name = 'player/video.html'
    ordering = ['-time_added']


class MusicList(ListView):
    model = Music
    template_name = 'player/audio.html'
    ordering = ['-time_added']

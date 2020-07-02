from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Video, Music


class VideoList(ListView):
    queryset = Video.objects.all().order_by('-time_added')
    template_name = 'player/video.html'
    paginate_by = 15


class VideoDetail(DetailView):
    model = Video
    template_name = 'player/video_detail.html'


class MusicList(ListView):
    model = Music
    template_name = 'player/audio.html'
    ordering = ['-time_added']


class MusicDetail(DetailView):
    model = Music
    template_name = 'player/audio_detail.html'

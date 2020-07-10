from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Video, Music, PopularVideo


class VideoList(ListView):
    queryset = Video.objects.filter(status=1).order_by('-time_added')
    template_name = 'player/video.html'
    paginate_by = 24


class VideoDetail(DetailView):
    model = Video
    template_name = 'player/video_detail.html'


def popular_video(request):
    video_list_tube = PopularVideo.objects.filter(
        status=1).order_by('-time_added')

    user_list = User.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'player/popular_video.html',
                  {'video_tube': video_list_tube,
                   'users': users})


class MusicList(ListView):
    model = Music
    template_name = 'player/audio.html'
    ordering = ['-time_added']
    paginate_by = 16


class MusicDetail(DetailView):
    model = Music
    template_name = 'player/audio_detail.html'

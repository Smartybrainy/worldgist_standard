from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from .models import Video, Music, PopularVideo, TrendingVideo


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
    try:
        paginator = Paginator(video_list_tube, 10)
        page = request.GET.get('page')
        video_list_tube = paginator.get_page(page)
    except PageNotAnInteger:
        messages.info(request, "page not in order")
        return redirect('player:popular-video')
    except EmptyPage:
        messages.info(request, "You are requesting an empty page!")
        return redirect('player:popular-video')

    return render(request, 'player/popular_video.html',
                  {'video_tube': video_list_tube})


class MusicList(ListView):
    model = Music
    template_name = 'player/audio.html'
    ordering = ['-time_added']
    paginate_by = 16


class MusicDetail(DetailView):
    model = Music
    template_name = 'player/audio_detail.html'


class TrendingVideosView(ListView):

    def get(self, *args, **kwargs):
        qs = TrendingVideo.objects.filter(status=1).order_by('-date_created')

        paginator = Paginator(qs, 20)
        page = self.request.GET.get('page')
        qs = paginator.get_page(page)

        context = {'object_list': qs}
        return render(self.request, 'player/trending.html', context)

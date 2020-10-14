from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField


STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

TRENDINGVIDEOSTATUS = (
    (0, 'Draft'),
    (1, "Publish")
)


class Video(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    desc = models.TextField(blank=True, null=True)
    video_file = models.FileField(
        upload_to="videos/%y/%m/%d/")
    time_added = models.DateTimeField()
    updated = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "List of videos"


class PopularVideo(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    desc = models.TextField(blank=True, null=True)
    url_video = models.CharField(max_length=2083, blank=True, null=True)
    time_added = models.DateTimeField()
    updated = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "List of popular videos"


class Music(models.Model):
    audio_img = models.ImageField(upload_to='Audio_pics')
    name = models.CharField(max_length=150, null=True, blank=True, unique=True)
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)
    desc = models.TextField(blank=True, null=True)
    audio_file = models.FileField(upload_to="Audios/%y/%m/%d/")
    time_added = models.DateTimeField()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "List of Audios"

    def get_absolute_url(self):
        return reverse('player:audio-detail', kwargs={
            'slug': self.slug
        })


class TrendingVideo(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    url_vid = EmbedVideoField()
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=TRENDINGVIDEOSTATUS, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Trending Videos"

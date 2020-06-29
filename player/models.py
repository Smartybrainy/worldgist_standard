from django.db import models
from django.utils import timezone


class Video(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    video_file = models.FileField(upload_to="videos/%y/%m/%d/")
    time_added = models.DateTimeField()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "List of videos"


class Music(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    audio_file = models.FileField(upload_to="Audios/%y/%m/%d/")
    time_added = models.DateTimeField()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "List of Audios"

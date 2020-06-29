from django.contrib import admin
from .models import Video, Music


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_file', 'time_added', 'updated',)


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'audio_file', 'time_added', 'updated',)

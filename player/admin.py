from django.contrib import admin
from .models import (Video,
                     Music,
                     PopularVideo)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_file', 'time_added', 'updated',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_filter = ('status',)


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'audio_file', 'audio_img',
                    'time_added', 'updated',)
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


class PopularVideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'url_video', 'time_added', 'updated',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_filter = ('status',)


admin.site.register(PopularVideo, PopularVideoAdmin)

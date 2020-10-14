from django.contrib import admin
from .models import (Video,
                     Music,
                     PopularVideo,
                     TrendingVideo
                     )
from embed_video.admin import AdminVideoMixin


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


@admin.register(TrendingVideo)
class TrendingVideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('title', 'description', 'url_vid')
    list_display_links = ('url_vid',)
    list_filter = ['status']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(PopularVideo, PopularVideoAdmin)

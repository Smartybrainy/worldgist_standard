from django.contrib import admin
from .models import (Post, Like, Comment, SideBar)
from embed_video.admin import AdminVideoMixin


class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('title', 'date_created', 'updated',
                    'status', 'author')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog_post', 'value')
    list_filter = ('value',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'added_date', 'approved_comment', 'comment_img')
    search_fields = ['author', 'body']


admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(SideBar)

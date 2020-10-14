from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace="core")),
    path('blog/', include('blog.urls', namespace="blog")),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('tracker/', include('tracker.urls', namespace="tracker")),
    path('reaction/', include('reaction.urls', namespace="reaction")),
    path('player/', include('player.urls', namespace="player")),
    path('chat/', include('chat.urls', namespace="chat")),

    # For Email reset
    path('accounts/', include('django.contrib.auth.urls')),
    # For the social login
    path('oauth/', include('social_django.urls', namespace="social")),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

from django.contrib import admin
from .models import History


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'user', 'time_viewed',)


admin.site.register(History, HistoryAdmin)

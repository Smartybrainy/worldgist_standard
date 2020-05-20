from django.contrib import admin
from .models import Reaction


class ReactionAdmin(admin.ModelAdmin):
    list_display = ('email', 'added_date', 'content', 'name')
    list_filter = ('status',)
    search_fields = ['content']


admin.site.register(Reaction, ReactionAdmin)

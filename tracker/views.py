from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, View

from .models import History


class HistoryList(ListView):
    template_name = 'tracker/history.html'

    def get_queryset(self, *args, **kwargs):
        user_history = History.objects.filter(
            user=self.request.user).order_by('-time_viewed')
        return user_history


def history_delete(request, page_id, *args, **kwargs):
    obj = get_object_or_404(History, pk=page_id)
    if obj is not None:
        obj.delete()
    return redirect('tracker:history-list')


class HistoryAlert(TemplateView, View):
    model = History
    template_name = 'tracker/tracker_alert.html'

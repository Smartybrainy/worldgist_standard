from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView, View
from django.views.generic.detail import SingleObjectMixin

from .models import History


class HistoryList(ListView):
    template_name = 'tracker/history.html'

    def get_queryset(self):
        user_history = History.objects.filter(
            user=self.request.user).order_by('-time_viewed')
        return user_history


# class HistoryDelete(SingleObjectMixin, View):
#     model = History

#     def get_object(self, request, *args, **kwargs):
#         obj = self.get_object()
#         if obj is not None:
#             obj.delete()
#         return redirect('tracker:history-list')


def history_delete(request, page_id):
    obj = get_object_or_404(History, pk=page_id)
    if obj is not None:
        obj.delete()
        return redirect('tracker:history-list')

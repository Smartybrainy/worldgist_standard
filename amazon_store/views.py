from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import AmazonStore


class StoreListView(ListView):
    model = AmazonStore
    paginate_by = 24
    ordering = ['-timestamp']


class StoreDetailView(DetailView):
    model = AmazonStore


def search_engine(request):
    query = request.GET.get('qs')
    if query is not None:
        search_list = AmazonStore.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)
        )
    return render(request, 'main/amazon_search_result.html',
                  {'search_list': search_list})

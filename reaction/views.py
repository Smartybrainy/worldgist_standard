from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone

from .models import Reaction
from tracker.mixins import ObjectViewedMixin


class ReactionList(generic.ListView):
    model = Reaction
    template_name = 'reaction/views.html'

    def get_queryset(self):
        reaction_list = Reaction.objects.filter(
            status=1).order_by('added_date')
        return reaction_list


def add_reaction(request):
    current_time = timezone.now()
    if request.method == 'POST':
        content = request.POST['content']
        visitor_name = request.POST['visitor_name']
        email = request.POST['email']
        created_objs = Reaction.objects.create(content=content, email=email,
                                               added_date=current_time, name=visitor_name)

    return redirect("reaction:reaction-list")

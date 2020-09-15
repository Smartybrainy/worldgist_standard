from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin
                                        )
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )

from django.db.models import Q
from django.core.paginator import Paginator

from .models import Post, Like, Comment, SideBar
from .forms import CommentForm
from tracker.mixins import ObjectViewedMixin


class PostListView(ListView):

    def get(self, *args, **kwargs):
        queryset = Post.objects.filter(status=1).order_by('-date_created')
        greetings = SideBar.objects.filter(
            status="P").order_by('-date_created')

        paginator = Paginator(queryset, 25)
        page = self.request.GET.get('page')
        queryset = paginator.get_page(page)

        context = {
            'object_list': queryset,
            'greetings': greetings
        }
        return render(self.request, "blog/post_list.html", context)


class PostDetailView(ObjectViewedMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'content', 'image']
    login_url = 'accounts/login/'
    redirect_field_name = '/post/new/'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def search_queryset(request):
    query = request.GET.get('qs')
    if query is not None:
        search_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    return render(request, 'main/search_result.html',
                  {'search_list': search_list})


def post_likes(request, *args, **kwargs):
    user = request.user
    if request.method == 'POST':
        like_id = request.POST.get('like_id')
        like_obj = Post.objects.get(pk=like_id)

        if user in like_obj.liked.all():
            like_obj.liked.remove(user)
        else:
            like_obj.liked.add(user)

        like, created = Like.objects.get_or_create(
            user=user, blog_post_id=like_id)
        if not created:
            if like.value == "Like":
                like.value = 'Unlike'
            else:
                like.value = "Like"

        like.save()
    return redirect("blog:post-detail", slug=like_obj.slug)


def add_comment_to_post(request, page_id, *args, **kwargs):
    post = get_object_or_404(Post, pk=page_id)
    if request.method == 'POST':
        form = CommentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('blog:post-detail', slug=post.slug)
    else:
        form = CommentForm(request.POST or None)
    return render(request, 'main/add_post_to_comment.html',
                  {'form': form, 'nav_post': post})


@login_required
def comment_approve(request, page_id):
    comment = get_object_or_404(Comment, pk=page_id)
    comment.approve()
    return redirect('blog:post-detail', slug=comment.post.slug)


@login_required
def comment_remove(request, page_id):
    comment = get_object_or_404(Comment, pk=page_id)
    comment.delete()
    return redirect('blog:post-detail', slug=comment.post.slug)


def privacy_policy(request):
    return render(request, 'main/privacy_policy.html')

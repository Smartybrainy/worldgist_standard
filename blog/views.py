from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth import views as auth_views
from django.db.models import Q

from .models import Post, Like, Comment
from .forms import CommentForm
from tracker.mixins import ObjectViewedMixin


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    template_name = 'main/home.html'
    paginate_by = 15


def search_queryset(request):
    query = request.GET.get('query')
    object_list = Post.objects.filter(
        Q(title__icontains='query') | Q(content__icontains="query")
    )
    if query in object_list:
        print(query)
        return redirect('/')
    else:
        print("does not exit")
    return render(request, 'main/home.html')


# def home(request):
#     qs = Post.objects.filter(status=1).order_by('-date_created')[:10]
#     user = request.user
#     context = {
#         'qs': qs,
#         'user': user
#     }
#     return render(request, 'main/home.html', context)


class PostDetail(ObjectViewedMixin, generic.DetailView):
    model = Post
    template_name = 'main/post_detail.html'


# def post_detail(request, page_id):
#     user = request.user
#     created_detail = Post.objects.filter(pk=page_id)
#     context = {
#         "created_detail": created_detail,
#         'user': user
#     }
#     return render(request, 'main/post_detail.html', context)


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
        form = CommentForm
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

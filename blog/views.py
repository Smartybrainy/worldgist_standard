from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post, Like, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt


def home(request):
    qs = Post.objects.filter(status=1).order_by('-date_created')
    user = request.user
    context = {
        'qs': qs,
        'user': user
    }
    return render(request, 'main/home.html', context)


def post_detail(request, page_id):
    user = request.user
    created_detail = Post.objects.filter(pk=page_id)
    context = {
        "created_detail": created_detail,
        "user": user
    }
    return render(request, 'main/post_detail.html', context)


def post_likes(request, page_id):
    user = request.user
    if request.method == 'POST':
        like_id = request.POST.get('like_id')
        like_obj = Post.objects.get(id=like_id)

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
    return HttpResponseRedirect(reverse("blog:post-detail", args=str(page_id)))


def add_comment_to_post(request, page_id):
    post = get_object_or_404(Post, pk=page_id)
    if request.method == 'POST':
        form = CommentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('blog:post-detail', page_id=post.pk)
    else:
        form = CommentForm
    return render(request, 'main/add_post_to_comment.html',
                  {'form': form, 'nav_post': post})


@login_required
def comment_approve(request, page_id):
    comment = get_object_or_404(Comment, pk=page_id)
    comment.approve()
    return redirect('blog:post-detail', page_id=comment.post.pk)


@login_required
def comment_remove(request, page_id):
    comment = get_object_or_404(Comment, pk=page_id)
    comment.delete()
    return redirect('blog:post-detail', page_id=comment.post.pk)

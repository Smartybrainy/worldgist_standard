from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    post_likes,
                    add_comment_to_post,
                    comment_approve,
                    comment_remove,
                    search_queryset,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    privacy_policy
                    )

app_name = 'blog'

urlpatterns = [
    path('post-list/', PostListView.as_view(), name="post-list"),
    path('post-detail/<slug>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post-detail/<slug>/update/',
         PostUpdateView.as_view(), name="post-update"),
    path('post-detail/<slug>/delete/',
         PostDeleteView.as_view(), name="post-delete"),

    path('<pk>/post/likes/', post_likes, name="post-likes"),
    path('<int:page_id>/comment/', add_comment_to_post,
         name="add-comment-to-post"),
    path('<int:page_id>/comment_approve',
         comment_approve, name="comment-approve"),
    path('<int:page_id>/comment_remove', comment_remove, name="comment-remove"),
    path('search/', search_queryset, name="search-query"),
    path('policy/', privacy_policy, name="policy"),
]

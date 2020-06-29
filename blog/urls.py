from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name="post-list"),
    path('<slug>/post_detail/',
         views.PostDetail.as_view(), name="post-detail"),
    path('<pk>/post_likes/', views.post_likes, name="post-likes"),
    path('<int:page_id>/comment/', views.add_comment_to_post,
         name="add-comment-to-post"),
    path('<int:page_id>/comment_approve', views.comment_approve,
         name="comment-approve"),
    path('<int:page_id>/comment_remove', views.comment_remove,
         name="comment-remove"),
    path('search/', views.search_queryset, name="search-query"),

    path('logo/', views.logo_image, name="logo")
]

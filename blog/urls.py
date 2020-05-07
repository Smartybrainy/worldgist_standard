from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name="post-list"),
    path('<int:page_id>/post_detail/', views.post_detail, name="post-detail"),
    path('<int:page_id>/post_likes/', views.post_likes, name="post-likes"),
    path('add_comment/<int:page_id>/comment/', views.add_comment_to_post,
         name="add-comment-to-post"),
    path('comment/<int:page_id>/comment_approve', views.comment_approve,
         name="comment-approve"),
    path('comment/<int:page_id>/comment_remove', views.comment_remove,
         name="comment-remove")
]

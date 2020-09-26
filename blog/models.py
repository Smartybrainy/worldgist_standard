from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

SIDEBAR_CHOICE = (
    ('D', 'Draft'),
    ('P', "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # content = models.TextField()
    content = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(
        upload_to='document/%y/%m/%d/', blank=True, null=True,
        width_field="width_field", height_field="height_field")
    # url_video = models.CharField(
    #     max_length=2083, blank=True, null=True)
    url_video = EmbedVideoField(blank=True, null=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post')
    updated = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=1)
    liked = models.ManyToManyField(
        User, blank=True, default=None, related_name='likes')

    class Meta:
        ordering = ['-date_created']

    class Meta:
        verbose_name_plural = 'List of posts'

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.liked.all().count()

    # the below function counts only the approved comments
    def my_approved_comments(self):
        return self.my_comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={'slug': self.slug})


LIKE_CHOICES = (
    ('Like', "Like"),
    ("Unlike", 'Unlike')
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,
                             default='LIke', max_length=10)

    def __str__(self):
        return str(self.blog_post)

    class Meta:
        verbose_name_plural = 'Likes Documentation'


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='my_comments')
    comment_img = models.ImageField(upload_to='comment_pic/%y/%m/%d/',
                                    null=True, blank=True,
                                    width_field="width_field",
                                    height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    author = models.CharField(max_length=150)
    body = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return '{}'.format(self.body)

    class Meta:
        verbose_name_plural = "Documentation of Comments"


class SideBar(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(
        auto_now_add=True)
    status = models.CharField(choices=SIDEBAR_CHOICE,
                              max_length=10, default="D")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "SideBar Greetings"

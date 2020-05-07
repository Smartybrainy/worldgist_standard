from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# The migration from :4 is perfect

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField(
        upload_to='document/%y/%m/%d/', blank=True, null=True,
        width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post')
    updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)
    liked = models.ManyToManyField(
        User, blank=True, default=None, related_name='likes')

    class Meta:
        ordering = ['-date_created']

    class Meta:
        verbose_name_plural = 'List of posts'

    def __str__(self):
        return self.title

    @property
    def nom_likes(self):
        return self.liked.all().count()

    # the below function counts only the approved comments
    def my_approved_comments(self):
        return self.my_comments.filter(approved_comment=True)


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
    added_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return '{}'.format(self.body)

    class Meta:
        verbose_name_plural = "Documentation of Comments"
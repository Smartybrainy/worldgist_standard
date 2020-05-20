from django.db import models
from django.contrib.auth.models import User

PUBLISH = (
    (1, 'Publish'),
    (0, 'Draft')
)


class Reaction(models.Model):
    content = models.TextField()
    email = models.EmailField(default='Anonymous@email.com')
    name = models.CharField(max_length=50, blank=True,
                            null=True, default='Anonymous')
    added_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=PUBLISH, default=1)

    def __str__(self):
        return '%s posted %s' % (self.email, self.added_date)

    class Meta:
        verbose_name_plural = "Documentation of Reactions"

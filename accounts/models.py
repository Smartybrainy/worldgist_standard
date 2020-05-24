from django.db import models
from django.contrib.auth.models import User
from PIL import Image


STATUS = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="worldgist.png",
                              upload_to="profile_pics",
                              width_field="width_field",
                              height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    gender = models.CharField(choices=STATUS, max_length=10)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name_plural = "User Profiles"

    # def save(self):  # THIS WORKS WHEN IMAGE IS SAVING FROM LOCAL-FILE SYSTEM
        # return super().save()

        # img = Image.open(self.image.path)
        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

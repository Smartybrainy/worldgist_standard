from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


AMAZON_STORE_LABEL = (
    ('N', "primary"),
    ('R', "warning"),
    ('O', "secondary")
)

AMAZON_STORE_CATEGORY = (
    ('E', "Electronics"),
    ('C', "Computers"),
    ('SH', "Smart Home"),
    ('A', "Arts & Crafts"),
    ('AT', "Automotive"),
    ('B', "Baby"),
    ('BP', "Beauty & personal care"),
    ('W', "Women's Fashion"),
    ('M', "Men's Fashion"),
    ('G', "Girl's Fashion"),
    ('H', 'Health and Household'),
    ('HK', 'Home and Kitchen'),
    ('I', 'Industrial and Scientific'),
    ('L', 'Luggage'),
    ('MT', 'Movies & Television'),
    ('P', 'Pet suppies'),
    ('S', "Software"),
    ('SO', 'Sports and Outdoor'),
    ('THM', 'Tools & Home Improvement'),
    ('TG', 'Toys and Games'),
    ('VG', 'Video Games'),
    ('BF', "Boy's Fashion"),

)

STORE_STATUS = (
    ('N', "New"),
    ("R", "Recent")
)


class AmazonStore(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    img = models.ImageField(upload_to='amazon_store',
                            height_field='height_field',
                            width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    amazon_affiliate_link = models.CharField(
        max_length=2083)
    description = RichTextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    shipping_country = models.CharField(max_length=20, blank=True, null=True)
    label = models.CharField(
        max_length=20, choices=AMAZON_STORE_LABEL, default='N')
    category = models.CharField(
        max_length=20, choices=AMAZON_STORE_CATEGORY, default='E')
    status = models.CharField(choices=STORE_STATUS, max_length=10, default='N')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Amazon Store'

    def get_absolute_url(self, **kwargs):
        return reverse('store:product-detail', kwargs={
            'slug': self.slug
        })

    ordering = ['-timestamp']

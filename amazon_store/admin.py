from django.contrib import admin
from .models import AmazonStore


@admin.register(AmazonStore)
class AmazonStoreAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'slug',
                    'user',
                    'price',
                    'discount_price',
                    'amazon_affiliate_link',
                    'label',
                    'category',)

    list_display_links = ('title',
                          'slug',
                          'user',
                          'price',
                          'discount_price',
                          'amazon_affiliate_link',
                          'discount_price',
                          'label',
                          'category',)
    search_fields = ['title', 'author']

    list_per_page = 50

    prepopulated_fields = {'slug': ('title',)}

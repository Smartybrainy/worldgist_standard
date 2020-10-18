from django.urls import path
from .views import StoreListView, StoreDetailView, search_engine

app_name = "store"

urlpatterns = [
    path('products/', StoreListView.as_view(), name="item-list"),
    path('product/<slug>/', StoreDetailView.as_view(), name="product-detail"),
    path('search/', search_engine, name="search-engine"),
]

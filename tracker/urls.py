from django.urls import path
from . import views

app_name = "tracker"

urlpatterns = [
    path('', views.HistoryList.as_view(), name="history-list"),
    path('<int:page_id>/delete/',
         views.history_delete, name="history-delete"),
    path('history/alert/', views.HistoryAlert.as_view(), name="history-alert")
]

from django.urls import path
from . import views


urlpatterns = [
    path("", views.new_2_home, name="new_2_home"),
    path("create", views.create, name="create"),
    path("<int:pk>", views.NewsDetailNews.as_view(), name="news-detail"),
    path("<int:pk>/update", views.NewsUpdateView.as_view(), name="news-update"),
    path("<int:pk>/delete", views.NewsDeleteView.as_view(), name="news-delete")
]

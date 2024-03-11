from django.urls import path

from list import views

app_name = "list"

urlpatterns = [
    path("", views.index, name="index"),
    path("tags/", views.TagListView.as_view(), name="tag-list")
]

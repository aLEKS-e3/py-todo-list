from django.urls import path

from list import views

app_name = "list"

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task-list"),
    path("tags/", views.TagListView.as_view(), name="tag-list"),

]

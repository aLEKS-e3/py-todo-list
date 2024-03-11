from django.urls import path

from list import views

app_name = "list"

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task-list"),
    path("tags/", views.TagListView.as_view(), name="tag-list"),
    path("tags/create/", views.TagCreateView.as_view(), name="tag-create"),
    path("create/", views.TaskCreateView.as_view(), name="task-create"),
    path(
        "is-done/<int:pk>/",
        views.get_task_done_or_undone,
        name="task-done"
    ),
    path(
        "update/<int:pk>/",
        views.TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "delete/<int:pk>/",
        views.TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tags/update/<int:pk>/",
        views.TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/delete/<int:pk>/",
        views.TagDeleteView.as_view(),
        name="tag-delete"
    ),
]

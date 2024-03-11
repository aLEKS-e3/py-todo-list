from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from list.models import Tag, Task
from list.forms import TaskForm, TagForm


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tag-list")


class TaskListView(generic.ListView):
    queryset = Task.objects.prefetch_related(
        "tags"
    ).order_by("is_done", "-date")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "list/task_form.html"
    success_url = reverse_lazy("list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:task-list")


def get_task_done_or_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("list:task-list"))

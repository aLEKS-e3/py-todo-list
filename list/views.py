from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from list.models import Tag, Task
from list.forms import TaskForm, TagForm


class TagListView(ListView):
    model = Tag


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("list:tag-list")


class TaskListView(ListView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:task-list")


def get_task_done_or_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("list:task-list"))

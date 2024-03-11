from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from list.models import Tag, Task
from list.forms import TaskForm


class TagListView(ListView):
    model = Tag


class TaskListView(ListView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:task-list")

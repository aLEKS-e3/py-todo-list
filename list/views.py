from django.shortcuts import render
from django.views.generic import ListView

from list.models import Tag


def index(request):
    return render(request, "list/index.html")


class TagListView(ListView):
    model = Tag


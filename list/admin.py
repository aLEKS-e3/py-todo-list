from django.contrib import admin

from list.models import Task, Tag

admin.site.register(Tag)


@admin.register(Task)
class DriverAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("tags",)

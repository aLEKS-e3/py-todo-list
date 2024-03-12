from django import forms

from list.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(required=False, widget=forms.SelectDateWidget)

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags",)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"

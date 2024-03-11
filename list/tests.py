from django.test import TestCase
from django.shortcuts import reverse

from list.models import Task, Tag

TASK_LIST = reverse("list:task-list")
TASK_IS_DONE = reverse("list:task-done", kwargs={"pk": 1})


class ListTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Easy")
        self.task1 = Task.objects.create(
            content="Become a president",
        )
        self.task2 = Task.objects.create(
            content="Drop out of the uni",
        )
        self.task1.tags.add(self.tag)
        self.task2.tags.add(self.tag)

    def test_task_list_url_response(self):
        response = self.client.get(TASK_LIST)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list/task_list.html")

    def test_task_list_has_tasks_all_sorted(self):
        response = self.client.get(TASK_LIST)
        all_tasks = Task.objects.order_by("-date", "-is_done")
        self.assertEqual(
            list(response.context["task_list"]),
            list(all_tasks)
        )

    def test_task_complete_undo_button(self):
        self.client.get(TASK_IS_DONE)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.is_done, True)

        self.client.get(TASK_IS_DONE)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.is_done, False)

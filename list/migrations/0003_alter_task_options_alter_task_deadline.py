# Generated by Django 5.0.2 on 2024-03-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("list", "0002_alter_task_content"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={},
        ),
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

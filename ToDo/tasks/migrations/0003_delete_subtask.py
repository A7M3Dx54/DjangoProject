# Generated by Django 4.2.7 on 2023-12-14 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_importance_subtask'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subtask',
        ),
    ]
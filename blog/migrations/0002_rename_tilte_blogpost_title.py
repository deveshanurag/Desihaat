# Generated by Django 4.2.7 on 2024-03-26 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blogpost", old_name="tilte", new_name="title",
        ),
    ]

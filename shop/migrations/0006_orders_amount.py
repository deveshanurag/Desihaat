# Generated by Django 4.2.7 on 2024-03-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_orderupdate"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="amount",
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]

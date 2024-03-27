# Generated by Django 4.2.7 on 2024-02-09 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_product_category_product_image_product_price_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("msg_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(default="", max_length=70)),
                ("phone", models.CharField(default="", max_length=70)),
                ("desc", models.CharField(default="", max_length=500)),
            ],
        ),
        migrations.RenameField(
            model_name="product", old_name="sub_category", new_name="subcategory",
        ),
    ]

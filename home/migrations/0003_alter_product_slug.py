# Generated by Django 4.2.5 on 2023-09-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product", name="slug", field=models.TextField(unique=True),
        ),
    ]

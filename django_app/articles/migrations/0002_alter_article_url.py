# Generated by Django 4.1.7 on 2023-03-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="url",
            field=models.URLField(max_length=500),
        ),
    ]

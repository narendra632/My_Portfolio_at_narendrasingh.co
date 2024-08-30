# Generated by Django 4.1.3 on 2023-08-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0008_remove_experience_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Portfolio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("filter", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="portfolio/")),
                ("description", models.TextField()),
            ],
        ),
    ]

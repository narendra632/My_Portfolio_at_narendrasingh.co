# Generated by Django 4.1.3 on 2023-08-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0014_about"),
    ]

    operations = [
        migrations.AddField(
            model_name="about",
            name="bgimage",
            field=models.ImageField(default="", upload_to="portfolio"),
        ),
    ]

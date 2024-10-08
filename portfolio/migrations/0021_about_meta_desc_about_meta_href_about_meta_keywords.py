# Generated by Django 4.1.3 on 2023-08-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0020_remove_portfolio_image_portfolio_image1_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="about",
            name="meta_desc",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="about",
            name="meta_href",
            field=models.URLField(default=""),
        ),
        migrations.AddField(
            model_name="about",
            name="meta_keywords",
            field=models.CharField(default="", max_length=300),
        ),
    ]

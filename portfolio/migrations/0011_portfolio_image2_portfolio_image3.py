# Generated by Django 4.1.3 on 2023-08-05 15:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0010_portfolio_category_portfolio_project_url_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="portfolio",
            name="image2",
            field=models.ImageField(blank=True, upload_to="portfolio"),
        ),
        migrations.AddField(
            model_name="portfolio",
            name="image3",
            field=models.ImageField(blank=True, upload_to="portfolio"),
        ),
    ]

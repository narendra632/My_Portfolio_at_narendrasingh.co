# Generated by Django 4.1.3 on 2023-08-04 06:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0002_rename_skill_skills"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Skills",
            new_name="Skill",
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-30 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quidditch", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="QuidditchTeams",
            new_name="Teams",
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-30 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="QuidditchTeams",
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
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("division", models.CharField(max_length=100)),
                ("wins", models.IntegerField()),
                ("losses", models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-30 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quidditch", "0002_rename_quidditchteams_teams"),
    ]

    operations = [
        migrations.CreateModel(
            name="Players",
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
                ("name", models.CharField(max_length=255)),
                ("position", models.CharField(max_length=255)),
                ("age", models.IntegerField()),
                ("injured_reserve_list", models.BooleanField()),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="player",
                        to="quidditch.teams",
                    ),
                ),
            ],
        ),
    ]

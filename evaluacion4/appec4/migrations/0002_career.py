# Generated by Django 4.1.3 on 2022-12-26 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appec4", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Career",
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
                ("name", models.CharField(max_length=50)),
                ("shortname", models.CharField(max_length=30)),
                ("description", models.TextField()),
                ("imagen", models.TextField()),
                ("state", models.CharField(max_length=15)),
            ],
        ),
    ]

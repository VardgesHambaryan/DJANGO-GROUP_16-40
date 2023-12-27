# Generated by Django 5.0 on 2023-12-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                (
                    "author",
                    models.CharField(max_length=50, verbose_name="Movie Author"),
                ),
                (
                    "title",
                    models.CharField(max_length=128, unique=True, verbose_name="Title"),
                ),
                ("genre", models.CharField(max_length=50, verbose_name="Genres")),
                ("year", models.PositiveIntegerField(verbose_name="Year")),
            ],
            options={
                "verbose_name": "Movie",
                "verbose_name_plural": "Movies",
            },
        ),
    ]

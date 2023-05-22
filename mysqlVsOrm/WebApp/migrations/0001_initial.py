# Generated by Django 4.1.5 on 2023-01-20 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Director",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
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
                ("movie_title", models.CharField(max_length=150)),
                ("release_year", models.IntegerField()),
                (
                    "director",
                    models.ForeignKey(
                        max_length=100,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="WebApp.director",
                    ),
                ),
            ],
        ),
    ]

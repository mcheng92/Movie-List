# Generated by Django 4.2 on 2023-04-17 01:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_director_movie_director"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="director",
        ),
        migrations.DeleteModel(
            name="Director",
        ),
    ]
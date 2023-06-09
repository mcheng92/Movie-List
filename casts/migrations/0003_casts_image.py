# Generated by Django 4.1.7 on 2023-04-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("casts", "0002_rename_casts_casts_movie_remove_casts_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="casts",
            name="image",
            field=models.ImageField(
                default="image/character/Luke_Skywalker.jpg",
                upload_to="image/characters",
            ),
            preserve_default=False,
        ),
    ]

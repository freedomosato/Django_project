# Generated by Django 4.1.2 on 2022-10-27 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_rename_artistid_song_artist_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='id',
        ),
        migrations.AlterField(
            model_name='song',
            name='artist_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-28 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0011_remove_lyrics_song_id_remove_song_artist_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='number_of_likes',
            new_name='likes',
        ),
    ]

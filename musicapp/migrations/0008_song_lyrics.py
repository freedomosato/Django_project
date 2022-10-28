# Generated by Django 4.1.2 on 2022-10-28 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0007_remove_song_artist_delete_lyrics_delete_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('date_realeased', models.DateField(default='', null=True)),
                ('number_of_likes', models.IntegerField(null=True)),
                ('artist', models.IntegerField(default='', null=True)),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Lyrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('song', models.IntegerField(null=True)),
                ('song_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song')),
            ],
        ),
    ]
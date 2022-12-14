# Generated by Django 4.1.2 on 2022-10-28 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0010_alter_song_artist_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lyrics',
            name='song_id',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist_id',
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artist',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lyrics',
            name='song',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='date_realeased',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='number_of_likes',
            field=models.IntegerField(),
        ),
    ]

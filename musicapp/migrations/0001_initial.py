# Generated by Django 4.1.2 on 2022-10-27 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=21)),
                ('last_name', models.CharField(max_length=21)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('date_realeased', models.DateField()),
                ('number_of_likes', models.IntegerField()),
                ('artist_id', models.IntegerField()),
                ('Artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Lyrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('song_id', models.IntegerField()),
                ('Song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song')),
            ],
        ),
    ]

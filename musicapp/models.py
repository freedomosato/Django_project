from django.db import models
from datetime import datetime

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length=21)
    last_name = models.CharField(max_length=21)
    age = models.IntegerField()

class Song(models.Model):
    artist= models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    date_realeased = models.DateField()
    likes = models.IntegerField()
    artist = models.IntegerField()
    
class Lyrics(models.Model):
    song = models.ForeignKey(Song, on_delete= models.CASCADE)
    content = models.CharField(max_length=200)
    song = models.IntegerField()
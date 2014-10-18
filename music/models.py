from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length = 100)
    img = models.TextField(blank = True, null = True)
    models.DateTimeField(auto_now_add = True)

class Album(models.Model):
    title = models.TextField()
    release_year = models.IntegerField()
    img = models.TextField(blank = True, null = True)
    added = models.DateTimeField(auto_now_add = True)

class Track(models.Model):
    name = models.TextField()
    album = models.ForeignKey(Album)
    artist = models.ManyToManyField(Artist)
    img = models.TextField(blank = True, null = True)
    duration = models.CharField(max_length = 10)
    bitrate = models.CharField(max_length = 10)
    release_year = models.IntegerField()
    added = models.DateTimeField(auto_now_add = True)
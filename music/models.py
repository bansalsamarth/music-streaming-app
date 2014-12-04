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
    album = models.ForeignKey(Album, blank = True, null = True)
    artist = models.ManyToManyField(Artist, blank = True, null = True)
    url = models.TextField(blank = True, null = True)
    img = models.TextField(blank = True, null = True)
    duration = models.CharField(max_length = 10, blank = True, null = True)
    bitrate = models.CharField(max_length = 10, blank = True, null = True)
    release_year = models.IntegerField(blank = True, null = True)
    added = models.DateTimeField(auto_now_add = True)

class RadioStations(models.Model):
    name = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = True)
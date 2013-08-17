from django.db import models
from django.contrib import admin
# Create your models here.
class Strim(models.Model):
    lastupdate = models.DateTimeField()
    lastvisit = models.DateTimeField()
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    user = models.CharField(max_length=200)
    url  = models.CharField(max_length=255)
    yturl = models.CharField(max_length=200)
    ytid = models.CharField(max_length=60)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    strim = models.ForeignKey(Strim)
    def __unicode__(self):
        return self.title

class StrimAdmin(admin.ModelAdmin):
    pass

class SongAdmin(admin.ModelAdmin):
    pass

admin.site.register(Strim, StrimAdmin)

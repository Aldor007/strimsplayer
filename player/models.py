from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify


class Strim(models.Model):
    lastupdate = models.DateTimeField(auto_now=True)
    lastvisit = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Strim, self).save(*args, **kwargs)


class Song(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    user = models.CharField(max_length=200)
    url = models.CharField(max_length=255)
    yturl = models.CharField(max_length=200)
    ytid = models.CharField(max_length=60)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    strim = models.ForeignKey(Strim)

    def __unicode__(self):
        return self.title


class StrimAdmin(admin.ModelAdmin):
    fields = ["name"]


class SongAdmin(admin.ModelAdmin):
    pass

admin.site.register(Strim, StrimAdmin)

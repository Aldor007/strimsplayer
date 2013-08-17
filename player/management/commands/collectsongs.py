#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from django.core.management.base import BaseCommand, CommandError
from player.models import Song, Strim
from player.utils import SongParser
from datetime import date, timedelta, datetime

class Command(BaseCommand):
    args = 'none'
    help = 'Collect songs for strims'

    def handle(self, *args, **options):
        strimy = Strim.objects.filter(lastvisit__range=(datetime.now()-timedelta(7),datetime.now())).order_by('-lastupdate')
        print(strimy)
        try:
            for strim in strimy:
                print 'http://strims.pl/s/'+strim.slug
                test  = SongParser(url='http://strims.pl/s/'+strim.slug+'/', strim=strim);
                test.run()
                strim.lastupdate = datetime.now()
                strim.save()
        except Exception as err:
            self.stdout.write(err)


        self.stdout.write('Successfully closed ')

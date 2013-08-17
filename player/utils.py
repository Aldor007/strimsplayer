# -*- coding: utf-8 -*-
import pycurl
import StringIO
import lxml.html
import operator
from models import Song
from datetime import date, timedelta, datetime
from urlparse import urlparse, parse_qs
from django.core.exceptions import ObjectDoesNotExist
import threading
import logging
import re

class DateHelper:
    @staticmethod
    def makeDate(indate):
        indate = indate.replace("dzisiaj", (date.today()).strftime('%d %m %Y '))
        indate = indate.replace("wczoraj", (date.today()-timedelta(1)).strftime(('%d %m %Y')))

        indate = indate.replace('Poniedziałek', 'Monday')
        indate = indate.replace('Tuesday', 'Wtorek')
        indate = indate.replace('Wednesday', 'Środa')
        indate = indate.replace('Thursday', 'Czwartek')
        indate = indate.replace('Monday', 'Piątek')
        indate = indate.replace('Saturday', 'Sobota')
        indate = indate.replace('Sunday', 'Niedziela')

        indate = indate.replace('stycznia', '01')
        indate = indate.replace('lutego', '02')
        indate = indate.replace('marca', '03')
        indate = indate.replace('kwietnia', '04')
        indate = indate.replace('maja',  '05')
        indate = indate.replace('czerwca', '06')
        indate = indate.replace('lipca', '07')
        indate = indate.replace('sierpnia', '08')
        indate = indate.replace('września', '09')
        indate = indate.replace('pażdziernika', '10')
        indate = indate.replace('listopda', '11')
        indate = indate.replace('grudnia', '12')
        return indate


minimum = 2


class SongParser(threading.Thread):
    "varible for curl result"
    buffer = StringIO.StringIO()
    curl = pycurl.Curl()

    def __init__(self, url, strim):
        threading.Thread.__init__(self)
        self.url = url
        self.buffer = StringIO.StringIO()
        self.curl = pycurl.Curl()
        self.curl.setopt(pycurl.URL, str(self.url))
        self.curl.setopt(pycurl.WRITEFUNCTION, self.buffer.write)
        self.strim = strim

    def run(self):
        self.curl.perform()
        html_string = self.buffer.getvalue()
        if not html_string:
            print("Pusto")
            self.curl.perform()
        try:
            szkielet = lxml.html.fromstring(html_string)
            lista = szkielet.cssselect('ul.contents li div.content')
            for element in lista:
                title = element.cssselect('a.content_title')[0].text_content().encode('utf-8')
                title = re.sub('\s+', ' ', title)
                user = element.cssselect('a.user_name span')[0].text_content()
                upvotes = element.cssselect('a.like span.content_vote_count')[0].text_content()
                downvotes = element.cssselect('a.dislike span.content_vote_count')[0].text_content()
                songdate = element.cssselect('ul span.color_gray span')[0].get('title')
                songdate = DateHelper.makeDate(songdate)
                domain = element.cssselect('h2 span.color_gray a')[0].text_content()
                url = element.cssselect('ul.content_info_actions li a')[0].get('href')
                yturl = element.cssselect('a.content_title')[0].get('href')
                if domain == 'youtube.com':
                    try:
                        exist = Song.objects.get(url=url)
                        exist.votes = int(upvotes)-int(downvotes)
                        exist.upvotes = int(upvotes)
                        exist.downvotes = int(downvotes)
                        exist.save()
                    except ObjectDoesNotExist:
                        url_data = urlparse(yturl)
                        query = parse_qs(url_data.query)
                        ytid = query["v"][0]
                        print domain
                        song = Song(title=title, user=user, upvotes=int(upvotes), downvotes=int(downvotes),\
                                date=datetime.strptime(songdate, '%d %m %Y %H:%M:%S'), url=url,yturl=yturl,\
                                ytid=ytid, strim=self.strim, votes=int(upvotes)-int(downvotes))
                        song.save()
        except Exception as err:
            logging.exception('Error %s', err)


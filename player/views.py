# Create your views her
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from player.models import Song, Strim
from datetime import date, timedelta, datetime
from django.core.exceptions import ObjectDoesNotExist
VALID_SORTS = {
        'date': "date",
        'votes': "votes"
        }
VALID_DIR = {
        'asc': "",
        'desc': "-"
        }
def index(request):
    sort = request.GET.get('sort')
    direction = request.GET.get('dir')
    try:
        order = ''.join((VALID_DIR[direction], VALID_SORTS[sort]))
    except KeyError:
        order = '-date'
    try:
        songsList = Song.objects.all().order_by(order)
    except TypeError:
        songsList = Song.objects.all().order_by('date')
    paginator = Paginator(songsList, 25)  # Show 25 contacts per page
    print(paginator.count)
    page = request.GET.get('page')
    try:
        songs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        songs = paginator.page(1)
        print("Page not integer")
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        songs = paginator.page(paginator.num_pages)
        print("Empty page")
    print(songs.has_next())
    return render_to_response('index.html', {"songs": songs, "request": request})


def ajax(request):
    return HttpResponse("Not ready")

def strim(request, slug):
    slug = slug.lower()
    try:
        strim = Strim.objects.get(slug = slug)
    except ObjectDoesNotExist:
        return HttpResponse("Strim nie istnieje")
    if not strim:
        return HttpResponse("Strim nie istnieje")
    today = datetime.now().date()
    print strim.lastvisit.date()
    print today
    if strim.lastvisit.date() < today:
        strim.lastvisit = datetime.now()
        strim.save()
    songsList = Song.objects.filter(strim = strim)
    
    paginator = Paginator(songsList, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    print(page)
    print(paginator)
    try:
        songs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        songs = paginator.page(1)
        print("Page not integer")
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        songs = paginator.page(paginator.num_pages)
        print("Empty page")
    return render_to_response('strim.html', {"songs": songs, "request": request, "strimname": strim.name})


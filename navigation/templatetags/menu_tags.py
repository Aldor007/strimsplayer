from django import template
from player.models import Strim
register = template.Library()

def nav_strims():
    strims = Strim.objects.all()
    return {'strims': strims}

register.inclusion_tag('strim_list.html')(nav_strims)

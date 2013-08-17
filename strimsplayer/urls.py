from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'player.views.index'),
    url(r'^ajax/$','player.views.ajax'),
    url(r'^s/(?P<slug>[a-zA-Z0-9_.-]+)/$','player.views.strim'),
    # url(r'^strimsplayer/', include('strimsplayer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

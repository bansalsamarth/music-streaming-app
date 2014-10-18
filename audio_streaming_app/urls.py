from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import music.urls as music_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'audio_streaming_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(music_urls)),
)

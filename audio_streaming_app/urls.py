from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout
import music.urls as music_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'audio_streaming_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login, {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout, {'template_name': 'logout.html'}),
    url(r'^', include(music_urls)),
)

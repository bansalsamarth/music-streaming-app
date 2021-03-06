from django.conf.urls import *

urlpatterns = patterns('music.views', 
    (r'^$', 'main_page'),
	(r'^browse$', 'browse_page'),
	(r'^music$', 'my_music'),
	(r'^create$', 'create_radio_page'),
	(r'^about$', 'about'),
	(r'^radio/(?P<username>\w*)$', 'radio_page'),
	(r'^radio_setup$', 'setup_radio'),
	(r'^search$', 'search_channel')
)

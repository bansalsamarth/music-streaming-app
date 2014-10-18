from django.conf.urls import *

urlpatterns = patterns('music.views', 
    (r'^$', 'main_page')
)

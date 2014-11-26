from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from music.tasks import streaming_server_setup

import shout
import sys
import string
import time

@login_required()
def main_page(request):
    return render(request, 'index.html', {'active':'home'}, context_instance = RequestContext(request))

@login_required()
def setup_radio(request):
	if request.method == "GET":
		"""try:
			songs = request.POST['songs']
		except:
			return HttpResponse("No Songs Selected")"""
		streaming_server_setup.delay(request.user.username, "songs")
		return HttpResponse("Radio started")
	else:
		return HttpResponse("Bad Request")

@login_required()
def radio_page(request, username):
	data = {
		'active':'home',
		'radio_url' : "http://localhost:8000/" + username
	}
	return render(request, 'radio.html', data, context_instance = RequestContext(request))	

@login_required()
def browse_page(request):
	return render(request, 'browse.html', {'active':'browse'}, context_instance = RequestContext(request))

@login_required()
def my_music(request):
	return render(request, 'music.html', {'active':'my_music'}, context_instance = RequestContext(request))

@login_required()
def featured_page(request):
	return render(request, 'featured.html', {'active':'featured'}, context_instance = RequestContext(request))

@login_required()
def about(request):
	return render(request, 'about.html', {'active':'about'}, context_instance = RequestContext(request))
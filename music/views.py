from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from music.tasks import streaming_server_setup
from music.models import RadioStations

import shout, sys, string, time, requests

@login_required()
def main_page(request):
    return render(request, 'index.html', {'active':'home'}, context_instance = RequestContext(request))

@login_required()
def setup_radio(request):
	if request.method == "GET":
		return HttpResponse("Bad Request")

	elif request.method == "POST":
		songs = request.POST.getlist('songs[]')
		r = RadioStations(name = request.user.username)
		r.save()
		streaming_server_setup.delay(request.user.username, songs, r.id)

		return HttpResponseRedirect("/radio/" + request.user.username)

@login_required()
def radio_page(request, username):
	radio_url = "http://localhost:8000/" + username
	#try to check if we can make a GET request and see if a channel is live or not.
	try:
		#Should return Status 404
		response = requests.get(url=radio_url, timeout=(1))
		live = False
	except:
		#Time Out Exception as request not completed within defined time, as data is beig transferred
		live = True

	data = {
		'active':'home',
		'radio_url' : radio_url,
		'status' : live
	}

	return render(request, 'radio.html', data, context_instance = RequestContext(request))	

@login_required()
def browse_page(request):
	r = RadioStations.objects.filter(active = True)
	return render(request, 'browse.html', {'active':'browse', 'stations':r}, context_instance = RequestContext(request))

@login_required()
def search_channel(request):
	channel = request.GET['channel']
	return HttpResponseRedirect('/radio/' + channel)

@login_required()
def my_music(request):
	return render(request, 'music.html', {'active':'my_music'}, context_instance = RequestContext(request))

@login_required()
def create_radio_page(request):
	return render(request, 'create_page.html', {'active':'create'}, context_instance = RequestContext(request))

@login_required()
def about(request):
	return render(request, 'about.html', {'active':'about'}, context_instance = RequestContext(request))
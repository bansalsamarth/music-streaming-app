from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def main_page(request):
    return render(request, 'index.html', {'active':'home'}, context_instance = RequestContext(request))
    #return HttpResponse("Hello World!")

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
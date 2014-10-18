from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.

def main_page(request):
    return render(request, 'index.html', {}, context_instance = RequestContext(request))
    #return HttpResponse("Hello World!")

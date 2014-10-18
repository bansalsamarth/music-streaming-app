from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def main_page(request):
    return render(request, 'index.html', {}, context_instance = RequestContext(request))
    #return HttpResponse("Hello World!")

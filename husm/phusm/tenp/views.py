from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def index(request):
    context = RequestContext(request)#obtem o contexto como detalhes da m'aquina do cliente'
    return render_to_response('index.html',context) 

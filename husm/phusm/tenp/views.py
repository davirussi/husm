from django.shortcuts import render_to_response
from django.template import RequestContext
from tenp.forms import PrescreverForm

# Create your views here.

def index(request):
    context = RequestContext(request)#obtem o contexto como detalhes da m'aquina do cliente'
    return render_to_response('index.html',context) 
    
def prescrever(request):
    context = RequestContext(request)#obtem o contexto como detalhes da m'aquina do cliente'
    if request.method == 'POST':
        form = PrescreverForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)    
        else:
            print form.errors   
    else:
        form = PrescreverForm()
    return render_to_response('prescrever.html',  {'form': form}, context) 

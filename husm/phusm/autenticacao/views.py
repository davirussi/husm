from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect #redirecionar browser para uma url diferente
from django.contrib import auth #build in authentication
from django.core.context_processors import csrf #token de autenticacao
#from django.contrib.auth.forms import UserCreationForm #criar o formulario de cadastro usando o auth build in do Django
from forms import MyRegistrationForm

# Create your views here.

# Sera necessario em todas as views que necessitam de login testar a existencia do elemento  if "state" in request.session:

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)
    
def auth_view(request):

    username = request.POST.get('username', '')# se nao existir username no POST coloca '' em username
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password) #retorna None caso nao encontre o usuario
    
    if user is not None:
        auth.login(request, user)
        request.session["state"]="logged"
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    if "state" in request.session:
        return render_to_response('loggedin.html',
                                {'full_name' : request.user.username})
    else:
        return HttpResponseRedirect('/accounts/login')
        

def invalid_login(request):
    return render_to_response('invalid_login.html')
    
def logout(request):
    auth.logout(request) #tambem apaga o dicionario de sessao
    return render_to_response('logout.html')



def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
            
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    
    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')

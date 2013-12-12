from django.conf.urls import patterns, url
from autenticacao import views

urlpatterns = patterns('',
        url(r'^login/$', 'autenticacao.views.login'),
        url(r'^auth/$', 'autenticacao.views.auth_view'),
        url(r'^logout/$', 'autenticacao.views.logout'),
        url(r'^loggedin/$', 'autenticacao.views.loggedin'),
        url(r'^invalid/$', 'autenticacao.views.invalid_login'),
        
        url(r'^register/$', 'autenticacao.views.register_user'),
        url(r'^register_success/$', 'autenticacao.views.register_success'),
        )

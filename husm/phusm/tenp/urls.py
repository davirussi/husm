from django.conf.urls import patterns, url
from tenp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
        url(r'^$',views.index,name='index'),
        )

from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minicms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','News.views.A'),

)



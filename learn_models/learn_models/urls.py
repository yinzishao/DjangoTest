from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learn_models.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'people.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

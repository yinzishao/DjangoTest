from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyFirst.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^add/$','MyTest.views.add',name='add'),
    url(r'^add2/(\d+)/(\d+)/$', 'MyTest.views.add2', name='add2'),
    url(r'^$', 'MyTest.views.home',name='home'),
    url(r'^index/$','MyTest.views.index',name='index'),
    url(r'^admin/', include(admin.site.urls)),
)

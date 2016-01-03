from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^here/$', here),
    url(r'^(\d{1,2})/math/(\d{1,2})/$',math),
]
from django.conf.urls import include, url
from . import views

urlpatterns = [
	# Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.post_list, name='post_list'),
    url(r'^rand/$', views.post_rand, name='post_rand'),
    url(r'^guess/1/$', views.post_guess1, name='post_guess1'),
    url(r'^guess/2/$', views.post_guess2, name='post_guess2'),
    url(r'^guess/3/$', views.post_guess3, name='post_guess3'),
    url(r'^guess/4/$', views.post_guess4, name='post_guess4'),
    url(r'^guess/5/$', views.post_guess5, name='post_guess5'),
    url(r'^guess/6/$', views.post_guess6, name='post_guess6'),
    url(r'^guess/7/$', views.post_guess7, name='post_guess7'),
    url(r'^guess/8/$', views.post_guess8, name='post_guess8'),
    url(r'^guess/9/$', views.post_guess9, name='post_guess9'),
    url(r'^guess/10/$', views.post_guess10, name='post_guess10'),
    url(r'^guess/11/$', views.post_guess11, name='post_guess11'),
    url(r'^guess/12/$', views.post_guess12, name='post_guess12'),
    url(r'^guess/13/$', views.post_guess13, name='post_guess13'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
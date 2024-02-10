# from django.conf.urls import url
from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^panel/$', views.panel, name='panel'),
    re_path(r'^login/$', views.mylogin, name='mylogin'),
    re_path(r'^logout/$', views.mylogout, name='mylogout'),
    re_path(r'^panel/setting/$', views.site_setting, name='site_setting'),
    re_path(r'^panel/change/pass/$', views.change_password, name='change_password'),
    re_path(r'^register/$', views.myregister, name='myregister'),
]
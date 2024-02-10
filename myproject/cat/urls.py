# from django.conf.urls import url
from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r'^panel/category/list', views.category_list, name='category_list'),
    re_path(r'^panel/category/create', views.category_create, name='category_create'),
    re_path(r'^panel/category/delete/(?P<pk>\d+)/$', views.category_delete, name='category_delete'),
]
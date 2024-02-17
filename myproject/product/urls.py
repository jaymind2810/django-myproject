# from django.conf.urls import url
from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r'^product_details/(?P<pk>\d+)/$', views.product_details, name='product_details'),
    re_path(r'^panel/product/list', views.product_list, name='product_list'),
    re_path(r'^panel/product/create', views.product_create, name='product_create'),
    re_path(r'^panel/product/delete/(?P<pk>\d+)/$', views.product_delete, name='product_delete'),
    re_path(r'^panel/product/edit/(?P<pk>\d+)/$', views.product_edit, name='product_edit'),
    re_path(r'^panel/product/publish/(?P<pk>\d+)/$', views.product_publish, name='product_publish'),
]
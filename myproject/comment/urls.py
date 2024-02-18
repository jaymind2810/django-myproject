# from django.conf.urls import url
from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r'^panel/comment/add/(?P<pk>\d+)$', views.product_comment_add, name='product_comment_add'),
    re_path(r'^panel/comment/del/(?P<pk>\d+)$', views.product_comment_delete, name='product_comment_delete'),
]
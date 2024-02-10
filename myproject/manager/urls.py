from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r'^panel/user/list', views.user_list, name='user_list'),
    re_path(r'^panel/user/delete/(?P<pk>\d+)/$', views.user_delete, name='user_delete'),
    re_path(r'^panel/manager/group/$', views.manager_group, name='manager_group'),
    re_path(r'^panel/manager/group/create', views.manager_group_create, name='manager_group_create'),
    re_path(r'^panel/manager/group/delete/(?P<name>.*)/$', views.manager_group_delete, name='manager_group_delete')
]
from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r'^panel/user/list', views.user_list, name='user_list'),
    re_path(r'^panel/user/delete/(?P<pk>\d+)/$', views.user_delete, name='user_delete'),
    re_path(r'^panel/manager/group/$', views.manager_group, name='manager_group'),
    re_path(r'^panel/manager/group/create', views.manager_group_create, name='manager_group_create'),
    re_path(r'^panel/manager/group/delete/(?P<name>.*)/$', views.manager_group_delete, name='manager_group_delete'),
    re_path(r'^panel/user/group/show/(?P<pk>\d+)/$', views.user_groups_show, name='user_groups_show'),
    re_path(r'^panel/user/addtogroup/(?P<pk>\d+)/$', views.add_user_to_groups, name='add_user_to_groups'),
    re_path(r'^panel/user/deletetogroup/(?P<pk>\d+)/(?P<name>.*)/$', views.delete_user_from_groups, name='delete_user_from_groups'),
    re_path(r'^panel/manager/perms/$', views.manager_perms, name='manager_perms'),
    re_path(r'^panel/manager/perms/delete/(?P<name>.*)/$', views.manager_perms_del, name='manager_perms_del'),
    re_path(r'^panel/manager/perms/create', views.manager_perms_create, name='manager_perms_create'),
    re_path(r'^panel/user/perms/show/(?P<pk>\d+)/$', views.user_perms_show, name='user_perms_show'),
    re_path(r'^panel/user/deleteperms/(?P<pk>\d+)/(?P<name>.*)/$', views.delete_user_perms, name='delete_user_perms'),
    re_path(r'^panel/user/addperms/(?P<pk>\d+)/$', views.add_perms_to_user, name='add_perms_to_user'),
    re_path(r'^panel/groups/perms/show/(?P<name>.*)/$', views.groups_perms_show, name='groups_perms_show'),
    re_path(r'^panel/groups/deleteperms/(?P<gname>.*)/(?P<name>.*)/$', views.delete_group_perms, name='delete_group_perms'),
    re_path(r'^panel/groups/addperms/(?P<gname>.*)/$', views.add_perms_to_group, name='add_perms_to_group'),
]
# from django.conf.urls import include, url
from django.urls import include, re_path
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('main.urls')),
# ]

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path('', include('main.urls')),
    re_path('', include('product.urls')),
    re_path('', include('cat.urls')),
    re_path('', include('manager.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
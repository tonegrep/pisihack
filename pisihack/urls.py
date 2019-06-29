from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('front.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

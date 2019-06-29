from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('front.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('user_profile.urls'))
]

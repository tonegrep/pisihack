from django.urls import include, path

import front

urlpatterns = [
    path('', include(front.urls))
]
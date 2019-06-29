from django.urls import path

from front.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
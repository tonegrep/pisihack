from django.urls import path

from projects.views import ProjectCreationView

urlpatterns = [
    path('create/', ProjectCreationView.as_view(), name='create'),
]

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('me/', TemplateView.as_view(template_name="profile.html")),
]
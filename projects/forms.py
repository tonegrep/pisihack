from django.forms import ModelForm
from .models import Project
class ProjectCreationForm(ModelForm):
    class Meta:
       model = Project
       fields = ('maintainer', 'vacant_slots', 'repos', 'status', 'progress') 
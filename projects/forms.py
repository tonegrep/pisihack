from django.forms import ModelForm

from .models import Project, Repository


class ProjectCreationForm(ModelForm):
    repos = Repository.objects.all()

    class Meta:
        model = Project
        fields = ('maintainer', 'vacant_slots', 'repos', 'status', 'progress')

    def __init__(self, *args, **kwargs):
        self.maintainer = kwargs.pop('maintainer')
        super().__init__(*args, **kwargs)

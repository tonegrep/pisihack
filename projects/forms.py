from django.forms import ModelForm, ModelMultipleChoiceField

from .models import Project, Repository


class ProjectCreationForm(ModelForm):
    repos = ModelMultipleChoiceField(queryset=None)

    class Meta:
        model = Project
        fields = ('vacant_slots', 'repos', 'status', 'progress')

    def __init__(self, *args, **kwargs):
        self.maintainer = kwargs.pop('maintainer')
        super().__init__(*args, **kwargs)

        self.fields['repos'].queryset = Repository.objects.filter(author=self.maintainer)

    def save(self, commit=True):
        instance = super().save(commit=False)
        print(dir(instance))
        instance.maintainer = self.maintainer
        if commit:
            instance.save()
        return instance

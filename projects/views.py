from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from .forms import ProjectCreationForm
from .models import Project


class ProjectCreationView(CreateView):
    template_name = 'new_project.html'
    form_class = ProjectCreationForm

    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = 'My Project'

        return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['maintainer'] = self.request.user

        return kwargs


class ProjectView(TemplateView):
    template_name = 'projects.html'

    def get(self, request, *args, **kwargs):
        cur_user = request.user
        user_projects = Project.objects.filter(user=cur_user)
        context = {
            'user_proj': user_projects,
        }
        return render(request, self.template_name, context)

# Create your views here.

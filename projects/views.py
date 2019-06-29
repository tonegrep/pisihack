from django.shortcuts import render
from .models import Project
from user_profile.models import Skill
from django.views.generic import TemplateView
from .forms import ProjectCreationForm

def find_best_projects(skills):
    Project.objects.filter()


class ProjectCreationView(TemplateView):
    template_name='new_project.html'
    form = ProjectCreationForm()
    def get(self, request, *args, **kwargs):
        if form.is_valid():
            form.save()
        return render(request, self.template_name, context)

class ProjectView(TemplateView):
    template_name = 'projects.html'
    def get(self, request, *args, **kwargs):
        cur_user = request.user
        user_projects = Project.objects.filter(user=cur_user)
        user_skills = Skill.objects.filter(user=cur_user).order_by(lvl)[:3]
        best_proj = find_best_projects(user_skills)
        context= {
            'best_proj' : best_proj,
            'user_proj' : user_projects,
        }
        return render(request, self.template_name, context)



# Create your views here.

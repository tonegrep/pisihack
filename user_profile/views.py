from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Skill, Subject
from projects.models import Repository
from users.models import PisiUser

class ProfileView(TemplateView):
    template_name="profile.html"
    def get(self, request, *args, **kwargs):
        cur_user = request.user
        skills = Skill.objects.filter(user=cur_user)
        subjects = Subject.objects.filter(user=cur_user)
        repos = Repository.objects.filter(user=cur_user)
        context = {
            'skills'   : skills,
            'subjects' : subjects,
            'repos'    : repos,
        }
        return render(request, self.template_name, context)




# Create your views here.

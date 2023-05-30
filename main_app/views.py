from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, TemplateView

from main_app.models import Memory


class MemoriesView(LoginRequiredMixin, ListView):
    model = Memory
    template_name = 'memories.html'
    context_object_name = 'memory'


class MemoryCreateView(LoginRequiredMixin, CreateView):
    model = Memory
    template_name = 'addmemory.html'
    fields = ['title', 'description', 'location']


class LoginView(TemplateView):
    template_name = 'login.html'

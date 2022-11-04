from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy
from Cadastros.models import Professor

class criarUsuario(CreateView):
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        url = super().form_valid(form)
        Professor.objects.create(Usuario = self.object)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

class updateUsuario(UpdateView):
    model = Professor
    fields=['Nome','DataNascimento','CPF','Titulacao']
    success_url = reverse_lazy('cursos')

    def get_object(self, queryset = None):
        self.object = get_object_or_404(Professor, Usuario = self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


from importlib.resources import path
from django.urls import path
from django.contrib.auth import views as views_autenticacao
from .views import criarUsuario, updateUsuario

urlpatterns = [
    path('login', views_autenticacao.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout', views_autenticacao.LogoutView.as_view(), name='logout'),
    path('registrar', criarUsuario.as_view(template_name='usuarios/criacaouser.html'), name='registrar'),
    path('cadastroprofessor', updateUsuario.as_view(template_name='usuarios/criacaouser.html'), name='cadastroprofessor')
]

from django import views
from django.urls import include, re_path, path
from Cadastros import views

urlpatterns=[
    path('', views.home, name='home'),
    re_path(r'^realizarcadastrocurso$', views.realizarCadastroCurso, name='realizarcadastrocurso'),

    re_path(r'^cadastroareatematica$', views.cadastroAreaTematica, name='cadastroareatematica'),

    re_path(r'^cadastrocertificado$', views.cadastroCertificado),
    re_path(r'^emitircertificado/([0-9]+)$', views.emitirCertificado, name='emitircertificado'),

    re_path(r'^topicosaula/([0-9]+)$', views.topicoAulaAPI, name='topicosaula'),
    re_path(r'^cadastrotopicosaula/([0-9]+)$', views.realizarCadastroTopicoAula, name='cadastrotopicosaula'),

    re_path(r'^professor$', views.professorAPI),
    re_path(r'^professor/([0-9]+)$', views.professorAPI),

    re_path(r'^areatematica$', views.areaTematicaAPI),
    re_path(r'^areatematica/([0-9]+)$', views.areaTematicaAPI),

    re_path(r'^cursos$', views.cursoAPI, name='cursos'),
    re_path(r'^edicaocurso/([0-9]+)$', views.editarCurso, name='edicaocurso'),

    re_path(r'^deletarcurso/([0-9]+)$', views.deletarCurso, name='deletarcurso'),

    re_path(r'^topicoaula$', views.topicoDeAulaAPI),
    re_path(r'^topicoaula/([0-9]+)$', views.topicoDeAulaAPI),

    re_path(r'^titulacao$', views.titulacaoAPI),
    re_path(r'^titulacao/([0-9]+)$', views.titulacaoAPI),

    re_path(r'^aprovarcurso/([0-9]+)$', views.aprovarCurso, name='aprovarcurso'),

    re_path(r'^validacaocertificado$', views.validacaoCertificado, name='validacaocertificado'),
    re_path(r'^validarcertificado$', views.validarCertificado, name='validarcertificado')
]

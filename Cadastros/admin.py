from django.contrib import admin
from .models import Certificado, AreaTematica, Curso, Professor, TopicoDeAula, Titulacao


admin.site.register(Certificado)
admin.site.register(AreaTematica)
admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(TopicoDeAula)
admin.site.register(Titulacao)


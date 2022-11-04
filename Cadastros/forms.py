from faulthandler import disable
from Cadastros.models import AreaTematica, Curso, Professor, Titulacao, TopicoDeAula, Certificado
from django import forms

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        exclude = ('Aprovado',)
        labels = {
            "Nome": "Nome do Curso",
            "CargaHoraria": "Carga Horária",
            "AreaTematica": "Área Temática",
            "ProfessorResponsavel": "Professor Responsável",
            "DataCriacao": "Data de Criação do plano de curso",
        }
        widgets = {
            '': forms.TextInput(),
            '': forms.IntegerField(),
            '': forms.ModelChoiceField(queryset=AreaTematica.objects.all()),
            '': forms.ModelChoiceField(queryset=Professor.objects.all()),
            '': forms.DateInput()
        }

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        exclude = ()
        labels = {
            "Nome": "Nome completo",
            "DataNascimento": "Data de nascimento",
            "CPF": "CPF",
            "Titulacao": "Titulação",
            "Senha": "Senha",
        }
        widgets = {
            '': forms.TextInput(),
            '': forms.DateField(),
            '': forms.TextInput(),
            '': forms.ModelChoiceField(queryset=Titulacao.objects.all()),
            '': forms.PasswordInput()
        }

class TopicoAulaForm(forms.ModelForm):
    class Meta:
        model = TopicoDeAula
        exclude = ()
        labels = {
            "Titulo": "Título",
            "Descricao": "Descrição",
            "Curso": "Curso"
        }
        widgets = {
            '': forms.TextInput(),
            '': forms.TextInput(),
            '': forms.ModelChoiceField(queryset=Curso.objects.all())
        }

class CertificadoForm(forms.Form):
    DataCriacao = forms.DateField(label="Data de emissão do certificado")
    CodigoValidacao = forms.CharField(label="Código de autenticação do certificado")

class AreaTematicaForm(forms.ModelForm):
    class Meta:
        model = AreaTematica
        exclude = ()
        labels = {
            "Nome": "Nome"
        }
        widgets = {
            '': forms.TextInput()
        }



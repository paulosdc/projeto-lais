from django.db import models
from django.contrib.auth.models import User
from cpf_field.models import CPFField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Titulacao(models.Model):
    TitulacaoID = models.AutoField(primary_key = True)
    Nome = models.CharField(max_length = 200)
    def __str__(self):
        return "%s" %(self.Nome)

class Professor(models.Model):
    ProfessorID = models.AutoField(primary_key = True)
    Nome = models.CharField(max_length = 200, null = True)
    DataNascimento = models.DateField(null = True)
    CPF = CPFField('cpf')
    Titulacao = models.ForeignKey(Titulacao, on_delete = models.PROTECT, null = True)
    Usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    def __str__(self):
        return "%s (%s)" %(self.Nome, self.CPF)

class AreaTematica(models.Model):
    AreaID = models.AutoField(primary_key = True)
    Nome = models.CharField(max_length = 200)
    def __str__(self):
        return "%s" %(self.Nome)

class Curso(models.Model):
    CursoID = models.AutoField(primary_key = True)
    Nome = models.CharField(max_length = 120)
    CargaHoraria = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(350)])
    AreaTematica = models.ForeignKey(AreaTematica, on_delete = models.PROTECT)
    ProfessorResponsavel = models.ForeignKey(Professor, on_delete = models.PROTECT)
    DataCriacao = models.DateField()
    Aprovado = models.BooleanField(null=True, default=None)
    def __str__(self):
        return "%s" %(self.Nome)

class TopicoDeAula(models.Model):
    TopicoID = models.AutoField(primary_key = True)
    Titulo = models.CharField(max_length = 120)  
    Descricao = models.CharField(max_length = 500)
    Curso = models.ForeignKey(Curso, on_delete = models.PROTECT)

class Certificado(models.Model):
    DataCriacao = models.DateField()
    CodigoValidacao = models.CharField(max_length = 200, primary_key = True)  
    def __init__(self, DataCriacao, CodigoValidacao):
        super().__init__(DataCriacao, CodigoValidacao)
        self.DataCriacao = DataCriacao
        self.CodigoValidacao = CodigoValidacao



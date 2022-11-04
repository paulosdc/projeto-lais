from dataclasses import field
from rest_framework import serializers
from Cadastros.models import AreaTematica, Certificado, Curso, Professor, Titulacao, TopicoDeAula

class AreaTematicaSerializer(serializers.ModelSerializer):
    class Meta:
        model=AreaTematica
        fields=('AreaID','Nome')

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Curso
        fields=('CursoID','Nome','CargaHoraria','AreaTematica','ProfessorResponsavel','DataCriacao','Aprovado')
    def update(self, instance, validated_data): 
        instance.Aprovado = validated_data.get('Aprovado', instance.Aprovado)
        instance.save()
        return instance

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Professor
        fields=('ProfessorID','Nome','DataNascimento','CPF','Titulacao', 'Usuario')

class CertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Certificado
        fields=('DataCriacao','CodigoValidacao')
      
class TopicoAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model=TopicoDeAula
        fields=('TopicoID','Titulo','Descricao','Curso')

class TitulacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Titulacao
        fields=('TitulacaoID','Nome')

               

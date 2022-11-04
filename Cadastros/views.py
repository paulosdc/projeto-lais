from django.shortcuts import redirect, render,  get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Cadastros.forms import CursoForm, TopicoAulaForm, CertificadoForm, AreaTematicaForm
from datetime import date
from reportlab.lib.utils import ImageReader
import numpy
import secrets
import math

# Imports pra gerar o pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter

from Cadastros.models import Certificado, Curso, TopicoDeAula, Professor
from Cadastros.serializers import CertificadoSerializer, CursoSerializer, AreaTematicaSerializer, ProfessorSerializer, TitulacaoSerializer, TopicoAulaSerializer
# Create your views here.

@csrf_exempt
def professorAPI(request):
    professor_dados = JSONParser().parse(request)
    professores_serializer = ProfessorSerializer(data = professor_dados, many = True)
    if professores_serializer.is_valid():
        professores_serializer.save()
        return JsonResponse("Cadastro realizado!", safe = False)
    return JsonResponse("Falha ao cadastrar", safe = False)


@csrf_exempt
def cursoAPI(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    if request.user.is_superuser == False:
        professor = Professor.objects.get(Usuario = request.user)
        if professor.Nome == None:
            return redirect('cadastroprofessor')
    if request.method == 'GET':
        if request.user.is_superuser == True:
            cursos = Curso.objects.all()
            nome = request.user.username
            idade = 0
            cpf = 0
        else:
            todos = Curso.objects.all()
            cursos = []
            for curso in todos:
                if curso.ProfessorResponsavel.Usuario == request.user:
                    cursos.append(curso)
            nome = professor.Nome
            idade = date.today() - professor.DataNascimento
            idade = idade.days / 365.25
            cpf = professor.CPF
        context = {
            'cursos': cursos,
            'nome': nome,
            'idade': math.floor(idade),
            'datanasc': professor.DataNascimento,
            'cpf': cpf
        }
        return render(request, 'projeto/cursos.html', context)   
        
    elif request.method == 'POST':
        curso_dados = JSONParser().parse(request)
        cursos_serializer = CursoSerializer(data = curso_dados, many = True)
        if cursos_serializer.is_valid():
            cursos_serializer.save()
            return JsonResponse("Cadastro realizado!", safe = False)
        return JsonResponse("Falha ao cadastrar", safe = False)


# Views das Áreas Temáticas
@csrf_exempt
def areaTematicaAPI(request):
    area_tematica_dados = JSONParser().parse(request)
    areas_tematicas_serializer = AreaTematicaSerializer(data = area_tematica_dados, many = True)
    if areas_tematicas_serializer.is_valid():
        areas_tematicas_serializer.save()
        return JsonResponse("Cadastro realizado!", safe = False)
    return JsonResponse("Falha ao cadastrar", safe = False)

# Views dos tópicos de aulas
@csrf_exempt
def topicoDeAulaAPI(request):
    topico_aula_dados = JSONParser().parse(request)
    topicos_aula_serializer = TopicoAulaSerializer(data = topico_aula_dados, many = True)
    if topicos_aula_serializer.is_valid():
        topicos_aula_serializer.save()
        return JsonResponse("Cadastro realizado!", safe = False)
    return JsonResponse("Falha ao cadastrar", safe = False)

# Views das titulacoes
@csrf_exempt
def titulacaoAPI(request):
    titulo_dados = JSONParser().parse(request)
    titulacoes_serializer = TitulacaoSerializer(data = titulo_dados, many = True)
    if titulacoes_serializer.is_valid():
        titulacoes_serializer.save()
        return JsonResponse("Cadastro realizado!", safe = False)
    return JsonResponse("Falha ao cadastrar", safe = False)

def home(request):
    return render(request, 'projeto/home.html')

def realizarCadastroCurso(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    form = CursoForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('cursos')
    context = {
        'form': form
    }
    return render(request, 'projeto/cadastrocurso.html', context)

def editarCurso(request, id):
    if request.user.is_authenticated == False:
        return redirect('login')
    curso = Curso.objects.get(CursoID = id)
    form = CursoForm(request.POST or None, instance = curso)
    if request.POST and form.is_valid():
        form.save()
        return redirect('cursos')
    context = {
        'form': form
    }
    return render(request, 'projeto/edicaocurso.html', context)

def deletarCurso(request, id):
    if request.user.is_authenticated == False:
        return redirect('login')
    curso = Curso.objects.get(CursoID = id)
    curso.delete()
    return redirect('cursos')

@csrf_exempt
def cadastroCertificado(certificado):
    certificado_serializer = CertificadoSerializer(data = certificado.__dict__)
    if certificado_serializer.is_valid():
        certificado_serializer.save()
        return JsonResponse("Cadastro realizado!", safe = False)
    return JsonResponse("Falha ao cadastrar", safe = False)

def emitirCertificado(request, id):
    if request.user.is_authenticated == False:
        return redirect('login')
    buf = io.BytesIO()
    canva = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    canva.drawImage
    objeto = canva.beginText()
    objeto.setTextOrigin(inch, inch)
    objeto.setFont("Helvetica", 14)

    curso = Curso.objects.get(CursoID = id)
    tokenValidacao = secrets.token_urlsafe()

    conteudo = [''] 
    conteudo.append(curso.ProfessorResponsavel.Nome + " - " + curso.ProfessorResponsavel.CPF)
    conteudo.append("")
    conteudo.append("Nome do curso: " + curso.Nome)
    conteudo.append("Área Temática: " + curso.AreaTematica.Nome)
    conteudo.append("Carga Horária: " + str(curso.CargaHoraria))
    conteudo.append("Data de criação: " + curso.DataCriacao.strftime("%d/%m/%Y"))
    conteudo.append("Data de emissão: " + date.today().strftime("%d/%m/%Y"))
    conteudo.append("Código de autenticação: " + tokenValidacao)

    for linha in conteudo:
        objeto.textLine(str(linha))

    imagem =  ImageReader(r"C:\Users\paulo\Desktop\DjangoAPI\Cadastros\assinatura_exemplo.jpg")
    canva.drawImage(
        imagem,
        220,
        200,
        200,
        200
    )

    canva.drawText(objeto)
    canva.showPage()
    canva.save()
    buf.seek(0)

    certificado = Certificado(date.today(), tokenValidacao)
    cadastroCertificado(certificado)

    return FileResponse(buf, as_attachment=True, filename="Certificado.pdf")

def topicoAulaAPI(request, id):
    if request.user.is_authenticated == False:
        return redirect('login')
    if request.method == 'GET': 
        topicos = TopicoDeAula.objects.filter(Curso = id)
        context = {
            'topicos': topicos, 
            'id': id,
            'quantidade': numpy.size(topicos)
        }
        return render(request, 'projeto/topicosaula.html', context)

def realizarCadastroTopicoAula(request, id):
    if request.user.is_authenticated == False:
        return redirect('login')
    topicoAulaAPI(request, id)
    form = TopicoAulaForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('topicosaula', id)
    context = {
        'form': form,
        'id': id
    }
    return render(request, 'projeto/cadastrotopicoaula.html', context)

def aprovarCurso(request, id):
    if request.user.is_authenticated == False:
        return redirect('login')
    form = TopicoAulaForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('topicosaula', id)
    context = {
        'form': form,
        'id': id
    }
    return render(request, 'projeto/cadastrotopicoaula.html', context)

def aprovarCurso(request, id):
    if request.user.is_authenticated == False:
        return redirect('login')
    curso = Curso.objects.get(CursoID = id)
    curso_dados = {
        'Nome': curso.Nome,
        'CargaHoraria': curso.CargaHoraria,
        'AreaTematica': curso.AreaTematica.AreaID,
        'ProfessorResponsavel': curso.ProfessorResponsavel.ProfessorID,
        'DataCriacao': curso.DataCriacao,
        'Aprovado': 'True'
    }
    curso_serializer = CursoSerializer(data = curso_dados, partial = True)
    if curso_serializer.is_valid():
        curso_serializer.update(curso, curso_dados)
    return redirect('cursos')

def validacaoCertificado(request):
    form = CertificadoForm()
    context = {
        'form': form,
        'inicio': True
    }
    return render(request, 'projeto/validarcertificado.html', context)

def validarCertificado(request):
    form = CertificadoForm(request.POST)
    if form.is_valid():
        data_criacao = form.cleaned_data['DataCriacao']
        codigo_validacao = form.cleaned_data['CodigoValidacao']
    certificado = Certificado.objects.filter(DataCriacao = data_criacao, CodigoValidacao = codigo_validacao)
    if certificado:
        valido = True
    else:
        valido = False
    context = {
        'form': form,
        'valido': valido,
        'inicio': False
    }
    return render(request, 'projeto/validarcertificado.html', context)

def cadastroAreaTematica(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    form = AreaTematicaForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('cursos')
    context = {
        'form': form
    }
    return render(request, 'projeto/cadastroareatematica.html', context)



    


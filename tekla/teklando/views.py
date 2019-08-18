from django.shortcuts import render
from django.db import connection
from teklando.models import Voluntario
from teklando.models import Sugerido

# Create your views here.


def index(request):
    return render(request, 'index.html')


def cadastro(request):
    contexto = {}
    if request.method == 'POST':
        voluntario = Voluntario()
        voluntario.nome = request.POST.get('nome')
        voluntario.sobrenome = request.POST.get('sobrenome')
        voluntario.email = request.POST.get('email')
        voluntario.senha = request.POST.get('senha')
        voluntario.telefone = request.POST.get('telefone')
        voluntario.celular = request.POST.get('celular')
        voluntario.genero = request.POST.get('genero')
        voluntario.data_nascimento = request.POST.get('data_nascimento')
        voluntario.endereco = request.POST.get('endereco')
        voluntario.numero = request.POST.get('numero')
        voluntario.complemento = request.POST.get('complemento')
        voluntario.cep = request.POST.get('cep')
        voluntario.bairro = request.POST.get('bairro')
        voluntario.cidade = request.POST.get('cidade')
        voluntario.estado = request.POST.get('estado')
        voluntario.disponibilidade = request.POST.get('disponibilidade')
        voluntario.escolaridade = request.POST.get('escolaridade')
        voluntario.objetivo = request.POST.get('objetivo')
        voluntario.save()
        contexto = {'msg':
                    'Cadastro Efetuado com Sucesso! Realize o seu Login!'
                    }
        return render(request, 'login.html', contexto)
    return render(request, 'cadastro.html')


def login(request):
    if request.method == 'POST':
        email_form = request.POST.get('email')
        senha_form = request.POST.get('senha')
        voluntario = Voluntario.objects.filter(
                                                email=email_form,
                                                senha=senha_form
                                                ).first()
        print('Iae meu bom amigo ', voluntario)

        if voluntario is None:
            contexto = {'notfound': 'Cadastre-se para ser um voluntario'}
            return render(request, 'cadastro.html', contexto)
        else:
            sugeridos = Sugerido.objects.select_related('atividades', 'voluntarios').filter(voluntarios__in=Voluntario.objects.filter(email=email_form))
            contexto = {'voluntario': voluntario, 'sugeridos': sugeridos}
            return render(request, 'voluntario.html', contexto)
    return render(request, 'login.html')


def lista_atividades(request):
    return render(request, 'atividades.html')

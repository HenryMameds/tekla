from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.db import connection, transaction

from teklando.forms import CustomUserCreationForm
from teklando.models import Voluntario
from teklando.models import Sugerido

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'cadastro.html'


def AtividadePageView(request):
    current_user = request.user
    print(current_user.username)
    cursor = connection.cursor()
    cursor.execute("SELECT v.username, a.nome, a.horario, a.descricao, e.nome FROM teklando_atividade_escolas tae INNER JOIN teklando_atividade a ON a.id = tae.atividade_id INNER JOIN teklando_escola e ON e.id = tae.escola_id INNER JOIN teklando_voluntario_atividades tva ON tva.atividade_id = a.id INNER JOIN teklando_voluntario v ON tva.voluntario_id = v.id WHERE v.username = %s", [current_user.username])
    row = cursor.fetchone()
    print('=======================')
    print(row)
    print('=======================')
    if row is not None:
        nome_atividade = row[1]
        horario_atividade = row[2]
        descricao_atividade = row[3]
        nome_escola = row[4]
        contexto = {'nome_atividade': nome_atividade,
                    'horario_atividade': horario_atividade,
                    'descricao_atividade': descricao_atividade,
                    'nome_escola': nome_escola,
                    }
        return render(request, 'atividades.html', contexto)
    else:
        msg = 'Você ainda não tem atividades cadastradas'
        print(msg)
        contexto = {'msg': msg}
        return render(request, 'atividades.html', contexto)


def VoluntarioPageView(request):
    current_user = request.user
    print(current_user.id)
    sugeridos = Sugerido.objects.select_related('atividades', 'voluntarios').filter(voluntarios__in=Voluntario.objects.filter(username=current_user.username))
    contexto = {'sugeridos': sugeridos}
    return render(request, 'voluntario.html', contexto)


def Cadastrar_Atividade(request, id):
    current_user = request.user
    print(current_user.id)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO teklando_voluntario_atividades(voluntario_id, atividade_id) VALUES(%s, %s)', [current_user.id, id])
    return redirect('/atividades')

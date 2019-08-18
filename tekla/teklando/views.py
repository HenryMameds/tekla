from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.db import connection

from teklando.forms import CustomUserCreationForm
from teklando.models import Voluntario
from teklando.models import Sugerido

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'index.html'


def VoluntarioPageView(request):
    current_user = request.user
    print(current_user.username)
    sugeridos = Sugerido.objects.select_related('atividades', 'voluntarios').filter(voluntarios__in=Voluntario.objects.filter(username=current_user.username))
    contexto = {'sugeridos': sugeridos}
    return render(request, 'voluntario.html', contexto)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'cadastro.html'


# def lista_atividades(request):
#     return render(request, 'atividades.html')

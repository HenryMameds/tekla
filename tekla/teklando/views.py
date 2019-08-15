from django.shortcuts import render
from teklando.models import Voluntario

# Create your views here.


def index(request):
    return render(request, 'index.html')

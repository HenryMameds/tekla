from django.urls import path
from teklando.views import index
from teklando.views import cadastro
from teklando.views import login

urlpatterns = [
    path('', index),
    path('cadastro', cadastro),
    path('login', login),
]

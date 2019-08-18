from django.urls import path
from teklando.views import index
from teklando.views import cadastro
from teklando.views import login
# from teklando.views import sugerido

urlpatterns = [
    path('', index),
    path('cadastro', cadastro),
    path('login', login)
    # path('voluntario', sugerido)
]

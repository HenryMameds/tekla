from django.urls import path
from teklando.views import index
from teklando.views import cadastro


urlpatterns = [
    path('', index),
    path('cadastro', cadastro)
]

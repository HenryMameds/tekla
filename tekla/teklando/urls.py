from django.urls import path
from teklando.views import HomePageView
from teklando.views import VoluntarioPageView
from teklando.views import SignUpView
# from teklando.views import lista_atividades

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('voluntario/', VoluntarioPageView, name='voluntario'),
    path('cadastro/', SignUpView.as_view(), name='cadastro'),
    # path('atividades', lista_atividades)
]

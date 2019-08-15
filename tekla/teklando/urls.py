from django.urls import path
from teklando.views import index


urlpatterns = [
    path('', index),
]

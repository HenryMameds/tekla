from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserCreationForm, CustomUserChangeForm
from teklando.models import Voluntario
from . import models

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = Voluntario
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


admin.site.register(Voluntario, CustomUserAdmin)
admin.site.register(models.Escola)
admin.site.register(models.Atividade)
admin.site.register(models.Sugerido)

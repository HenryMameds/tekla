# Generated by Django 2.2.4 on 2019-08-16 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teklando', '0003_atividade_escolas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividade',
            name='escola',
        ),
    ]
# Generated by Django 2.2.4 on 2019-08-16 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teklando', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AddField(
            model_name='voluntario',
            name='senha',
            field=models.CharField(default=0, max_length=15, verbose_name='Senha'),
            preserve_default=False,
        ),
    ]
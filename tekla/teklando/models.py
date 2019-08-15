from django.db import models


class Voluntario(models.Model):
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )

    ESTADOS = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('PR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )

    DISPONIBILIDADES = (
        ('ST', 'Sábado Tarde'),
        ('SM', 'Sábado Manhã'),
        ('DT', 'Domingo Tarde'),
        ('DM', 'Domingo Manhã'),
    )

    ESCOLARIDADES = (
        ('M', 'Médio'),
        ('T', 'Técnico'),
        ('G', 'Graduação'),
        ('PG', 'Pós-Graduação'),
    )

    nome = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )

    sobrenome = models.CharField(
        max_length=255,
        verbose_name='Sobrenome'
    )

    email = models.EmailField(
        max_length=255,
        verbose_name='E-mail'
    )

    telefone = models.CharField(
        max_length=255,
        verbose_name='Telefone',
        blank=True,
        null=True
    )

    celular = models.CharField(
        max_length=255,
        verbose_name='Celular'
    )

    genero = models.CharField(
        max_length=255,
        verbose_name='Gênero',
        choices=GENEROS
    )

    data_nascimento = models.DateField(
        verbose_name=' Data de Nascimento'
    )

    endereco = models.CharField(
        max_length=255,
        verbose_name='Endereço'
    )

    numero = models.CharField(
        max_length=255,
        verbose_name='Número'
    )

    complemento = models.CharField(
        max_length=255,
        verbose_name='Complemento'
    )

    cep = models.CharField(
        max_length=255,
        verbose_name='CEP'
    )

    bairro = models.CharField(
        max_length=255,
        verbose_name='Bairro'
    )

    cidade = models.CharField(
        max_length=255,
        verbose_name='Cidade'
    )

    estado = models.CharField(
        max_length=255,
        verbose_name='Estado',
        choices=ESTADOS
    )

    disponibilidade = models.CharField(
        max_length=255,
        verbose_name='Disponibilidade',
        choices=DISPONIBILIDADES,
    )

    escolaridade = models.CharField(
        max_length=255,
        verbose_name='Escolaridade',
        choices=ESCOLARIDADES
    )

    objetivo = models.TextField()

    data_de_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome


class Login(models.Model):
    nome_usuario = models.CharField(
        max_length=30,
        verbose_name='Nome do Usúario'
    )

    senha = models.CharField(
        max_length=15,
        verbose_name='Senha'
    )


class Escola(models.Model):
    ESTADOS = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('PR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )

    nome = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )

    endereco = models.CharField(
        max_length=255,
        verbose_name='Endereço'
    )

    numero = models.CharField(
        max_length=255,
        verbose_name='Número'
    )

    cep = models.CharField(
        max_length=255,
        verbose_name='CEP'
    )

    bairro = models.CharField(
        max_length=255,
        verbose_name='Bairro'
    )

    cidade = models.CharField(
        max_length=255,
        verbose_name='Cidade'
    )

    estado = models.CharField(
        max_length=255,
        verbose_name='Estado',
        choices=ESTADOS
    )

    data_de_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)


class Atividade(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name='Atividade'
    )

    horario = models.DateField(
        verbose_name='Horário'
    )

    escola = models.CharField(
        max_length=255,
        verbose_name='Escola'
    )

    descricao = models.TextField()

    data_de_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

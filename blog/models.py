from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# --- Adicione o novo modelo aqui ---

class Pessoa(models.Model):
    Nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=14, unique=True)
    Email = models.EmailField(unique=True)
    Telefone = models.CharField(max_length=15)
    Data_de_nascimento = models.DateField()
    RG = models.CharField(max_length=12, unique=True)
    Endereco = models.CharField(max_length=200)
    Bairro = models.CharField(max_length=100)

    def __str__(self):
        return self.Nome
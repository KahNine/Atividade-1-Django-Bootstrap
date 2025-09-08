from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Pessoa

def tela_de_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(request, username=email, password=senha)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        # Adicione esta linha para ver todos os dados recebidos
        print("Dados do formulário:", request.POST)

        # Captura os dados do formulário
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirma_senha')

        # Verifica se as senhas existem e se são iguais
        if senha and senha == confirma_senha:
            # Continua com o cadastro
            nome = request.POST.get('nome')
            cpf = request.POST.get('cpf')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')
            data_nascimento = request.POST.get('data_nascimento')
            rg = request.POST.get('rg')
            endereco = request.POST.get('endereco')
            bairro = request.POST.get('bairro')
            
            try:
                user = User.objects.create_user(username=email, password=senha)
                user.save()

                Pessoa.objects.create(
                    Nome=nome,
                    CPF=cpf,
                    Email=email,
                    Telefone=telefone,
                    Data_de_nascimento=data_nascimento,
                    RG=rg,
                    Endereco=endereco,
                    Bairro=bairro,
                )
            except Exception as e:
                return render(request, 'cadastro.html', {'error': 'Este e-mail já está cadastrado.'})

            return redirect('login')
        else:
            # Retorna um erro se as senhas não coincidirem ou estiverem vazias
            return render(request, 'cadastro.html', {'error': 'As senhas não coincidem ou estão vazias.'})

    return render(request, 'cadastro.html')
        
def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    context = {
        'pessoas': pessoas
    }
    return render(request, 'listar_pessoas.html', context)

def home(request):
    return render(request, 'home.html')

def recuperar_senha(request):
    return render(request, 'recuperar_senha.html')
    
def perfil(request):
    if request.user.is_authenticated:
        try:
            pessoa = Pessoa.objects.get(Email=request.user.email)
            context = {
                'pessoa': pessoa
            }
            return render(request, 'perfil.html', context)
        except Pessoa.DoesNotExist:
            return redirect('home')

    return redirect('login')

def logout_view(request):
    auth_logout(request)
    return redirect('login')
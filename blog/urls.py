from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.tela_de_login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('pessoas/', views.listar_pessoas, name='listar_pessoas'),
    path('recuperar_senha/', views.recuperar_senha, name='recuperar_senha'),
    path('perfil/', views.perfil, name='perfil'),
    path('', views.tela_de_login, name='root'),
]

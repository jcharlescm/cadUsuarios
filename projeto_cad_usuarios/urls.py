
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, views responsavel, nome de referencia
    # usuarios.com   -- exemplo
    path('', views.home, name='home'),
    path('usuarios/emails.html', views.lista_emails, name='lista_emails'),    
    path('usuarios/usuarios.html', views.lista_usuarios, name='lista_usuarios'),    
    path('usuarios', views.usuarios, name='listagem_usuarios'),
    # http://seu_dominio/assinatura_email, função ou classe view , Dá um nome à URL
    path('emails', views.inclui_emails, name='inclui_email')    
]

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, views responsavel, nome de referencia
        path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('usuarios/login.html', views.logar, name='login'),    
    path('usuarios/emails.html', views.lista_emails, name='lista_emails'),    
    path('usuarios/usuarios.html', views.lista_usuarios, name='lista_usuarios'),    
    path('usuarios', views.usuarios, name='listagem_usuarios'),
    # http://seu_dominio/assinatura_email, função ou classe view , Dá um nome à URL
    path('emails', views.inclui_emails, name='inclui_email'),  
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(success_url='password_change_done'),
        name='password_change'
        # template_name = "registration/password_change_form.html"
    ),  
     
]

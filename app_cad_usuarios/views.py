from django.shortcuts import render
from .models import Usuario, EmailSubscription
from django.contrib import messages
from django.utils.timezone import now

def home(request):
    return render(request, 'usuarios/home.html')

def lista_emails(request):
    print(' chamando lista de e-mails 10 10')
    emails = {
        'emails': EmailSubscription.objects.all()
    }    
    return render(request, 'usuarios/emails.html', emails)

def lista_usuarios(request):
    print(' chamando lista de usuarios 17 17 ')
    usuarios = {
        'usuarios': Usuario.objects.all()
    }    
    return render(request, 'usuarios/usuarios.html', usuarios)

def usuarios(request):
    # Salvar os dados da tela para o BD
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    # Exibis todos usuarios em uma nova pag.
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    # Retornar os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)

def inclui_emails(request):
    if request.method == 'POST':        
        email = request.POST.get('email')

        if email:
            # Tenta encontrar o email e atualiza a data se ele existir
            contato, created = EmailSubscription.objects.get_or_create(email=email)    
            if not created:              
                contato.data = now()  # Atualiza a data para o horário atual
                contato.save()
                messages.success(request, 'Obrigado! Seu E-mail foi atualizado, você continuará recebendo ofertas exclusivas da Zeus Tech.')                    
            else:
                messages.success(request, 'Obrigado! Seu E-mail foi atualizado, você continuará recebendo ofertas exclusivas da Zeus Tech.')  

    # Retornar os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/home.html')

def logar(request):
    return render(request, 'usuarios/login.html')




from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

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






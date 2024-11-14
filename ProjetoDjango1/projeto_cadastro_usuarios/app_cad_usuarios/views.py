from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html') 

def usuarios(request):
    #salva dados da tela para o banco
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    #exibe todos os dados ja cadastrados
    usuarios={
        'usuarios':Usuario.objects.all()
    }

    #retornar para a pagina de listagem de usuarios
    return render(request,'usuarios/usuarios.html',usuarios)

def excluir_usuario(request, id):
    usuario = get_object_or_404(Pessoa, id=id)
    usuario.delete()
    return redirect('listagem_usuarios') 
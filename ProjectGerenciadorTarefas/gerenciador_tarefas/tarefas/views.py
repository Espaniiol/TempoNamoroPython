from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all() # obter todas as tarefas do banco de dados
    return render(request,'tarefas/lista_tarefas.html',{'tarefas':tarefas})

def adicionar_tarefa(request):
    if request.method == 'POST':
        titulo =request.POST.get('titulo') # obter o titulo do formulario
        if titulo:
            Tarefa.objects.create(titulo=titulo) # criar uma nova tarefa
        return redirect('lista_tarefas')
    return render(request,'tarefas/adicionar_tarefa.html')

def excluir_tarefa(request,id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete() # excluir tarefa
    return redirect('lista_tarefas')

def conferir_tarefa(request, id):
    # Busca a tarefa pelo ID
    tarefa = get_object_or_404(Tarefa, id=id)
    # Altera o status para concluída
    tarefa.concluida = True
    tarefa.save()
    # Redireciona para a lista de tarefas
    return redirect('lista_tarefas')

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})

from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

def home(request):
    return render(request, 'produtos/home.html',{'home': home})

def lista_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produto.html',{'produtos' : produtos})

def cadastrar_produto(request):

    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        form.save()
        return redirect('lista_produto')
    else: 
        form = ProdutoForm()
    return render(request, 'produtos/cadastrar_produto.html', {'form': form})


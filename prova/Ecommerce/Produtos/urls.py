from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('produtos/',views.lista_produto, name='lista_produto'),
    path('produtos/cadastrar/',views.cadastrar_produto, name='cadastrar_produto'),
]

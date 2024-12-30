from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('conferir/<int:id>/', views.conferir_tarefa, name='conferir_tarefa'),  # Nova rota
]

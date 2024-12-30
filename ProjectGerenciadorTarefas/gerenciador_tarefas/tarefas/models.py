from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100) # Campo de texto com limite de 100 caracteres
    concluida = models.BooleanField(default=False) # Indica se a tarefa foi concluida ou nao

    def __str__(self):
        return  self.titulo
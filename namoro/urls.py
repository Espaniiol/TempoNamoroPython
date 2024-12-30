from django.urls import path
from .views import tempo_de_namoro_view

urlpatterns = [
    path('', tempo_de_namoro_view, name='tempo_de_namoro'),
]

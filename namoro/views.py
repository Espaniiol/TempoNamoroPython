from django.shortcuts import render
from datetime import datetime

def tempo_de_namoro_view(request):
    data_inicio = datetime(2024, 1, 14, 14, 5, 0)  # Substitua pela data de início do namoro
    agora = datetime.now()

    # Calculando a diferença
    delta = agora - data_inicio
    anos = delta.days // 365 if delta.days >= 365 else None
    meses = (delta.days % 365) // 30
    dias = (delta.days % 365) % 30

    horas = delta.seconds // 3600
    minutos = (delta.seconds % 3600) // 60
    segundos = delta.seconds % 60

    return render(request, 'namoro/tempo_de_namoro.html', {
        'anos': anos,
        'meses': meses,
        'dias': dias,
        'horas': horas,
        'minutos': minutos,
        'segundos': segundos,
    })

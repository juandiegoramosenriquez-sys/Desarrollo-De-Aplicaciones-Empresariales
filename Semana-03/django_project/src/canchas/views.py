from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Cliente, Horario, Reserva

# Create your views here.
def reserva_create(request):
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        horario_id = request.POST['horario']
        Reserva.objects.create(cliente_id=cliente_id, horario_id=horario_id)
        return redirect('reserva_list')

    clientes = Cliente.objects.all()
    horarios = Horario.objects.filter(disponible=True)
    return render(request, 'canchas/reserva_form.html', {
        'clientes': clientes,
        'horarios': horarios,
    })
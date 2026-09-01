from django.shortcuts import redirect, render

from .forms import OrderForm
from .models import Cliente, Pedido, Pizza


def order_list(request):
    pedidos = Pedido.objects.select_related('cliente', 'pizza').all()
    return render(request, 'order/order_list.html', {'orders': pedidos})


def order_create(request):
    form = OrderForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        cliente, _ = Cliente.objects.get_or_create(
            nombre=form.cleaned_data['customer_name'],
            defaults={'telefono': form.cleaned_data['phone']}
        )

        pizza, _ = Pizza.objects.get_or_create(
            nombre=form.cleaned_data['pizza_name'],
            defaults={
                'tipo_masa': 'Masa tradicional',
                'ingredientes': 'Sin especificar',
                'estado_stock': 'Disponible',
            }
        )

        Pedido.objects.create(
            cliente=cliente,
            pizza=pizza,
            direccion_entrega=form.cleaned_data['address'],
            estado=form.cleaned_data['status'],
        )
        return redirect('order_list')

    return render(request, 'order/order_create.html', {'form': form})
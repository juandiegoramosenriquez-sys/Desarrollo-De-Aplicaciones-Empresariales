from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre


class Pizza(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_masa = models.CharField(max_length=50)
    ingredientes = models.TextField()
    estado_stock = models.CharField(
        max_length=20,
        choices=[
            ('Disponible', 'Disponible'),
            ('Poco stock', 'Poco stock'),
            ('Agotado', 'Agotado'),
        ],
        default='Disponible'
    )

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En preparación', 'En preparación'),
        ('Entregado', 'Entregado'),
        ('Cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )
    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.PROTECT,
        related_name='pedidos'
    )
    direccion_entrega = models.CharField(max_length=200)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='Pendiente'
    )

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    @property
    def customer_name(self):
        return self.cliente.nombre

    @property
    def phone(self):
        return self.cliente.telefono

    @property
    def pizza_name(self):
        return self.pizza.nombre

    @property
    def address(self):
        return self.direccion_entrega

    @property
    def status(self):
        return self.estado

    def __str__(self):
        return f'Pedido #{self.id} - {self.cliente.nombre}'


def _get_orders_db_from_models():
    orders = []
    for pedido in Pedido.objects.select_related('cliente', 'pizza').all():
        orders.append({
            'customer_name': pedido.customer_name,
            'phone': pedido.phone,
            'pizza_name': pedido.pizza_name,
            'address': pedido.address,
            'status': pedido.status,
        })
    return orders


# Compatibilidad con la versión anterior del proyecto.
# La carga directa desde la base de datos no debe hacerse al importar el módulo,
# porque Django aún no ha finalizado la inicialización de apps.
ORDERS_DB = []
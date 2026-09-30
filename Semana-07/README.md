# 🍕 Semana 07 · Lab 07: ORM avanzado en Django

**Curso:** Desarrollo de Aplicaciones Empresariales
**Proyecto:** Pizzería Online (Django 5.2 · SQLite)
**Código:** [`django_project/`](django_project/)

En este laboratorio se aplicó el ORM avanzado de Django sobre la aplicación `pizzeria`: transacciones seguras con `transaction.atomic()` y `F()`, reportes con `aggregate()` y `annotate()`, QuerySets personalizados con `as_manager()` y la optimización del problema N+1 con `select_related()` y `prefetch_related()`.

---

## 🗂️ Modelo de datos

| Rol | Entidad |
|---|---|
| Entidad principal | `Pedido` |
| Relación OneToOne | `DatosEntrega` ↔ `Cliente` |
| ForeignKey (1:N) | `Pedido` → `Cliente`, `MetodoPago`, `Repartidor` · `Pizza` → `Categoria` |
| ManyToMany con `through` | `Pedido` ↔ `Pizza` (vía `DetallePedido`) · `Pizza` ↔ `Ingrediente` (vía `RecetaPizza`) |

**Campos clave del laboratorio**

| Concepto | Campo |
|---|---|
| Campo entero que se descuenta | `Ingrediente.stock` |
| Campo de estado | `Pedido.estado` (pendiente, en preparación, en camino, entregado, cancelado) |
| Atributos del modelo intermedio | `DetallePedido.cantidad`, `DetallePedido.precio_unitario`, `RecetaPizza.cantidad_gramos` |

---

## 🔒 Operación transaccional: registrar pedido

- **URL:** `/pedidos/registrar/` · **Vista:** `pedido_registrar` · **Template:** `pedido_registrar.html` (hereda de `base.html`)
- Dentro de `transaction.atomic()`:
  1. Crea el `Pedido`.
  2. Crea su `DetallePedido`.
  3. Descuenta `Ingrediente.stock` con `F('stock') - necesario`, según la receta de la pizza.
- Si falta stock de algún ingrediente se lanza `StockInsuficiente`: se hace **rollback** de todo y el error se muestra en el mismo formulario.
- Si todo sale bien se aplica **Post/Redirect/Get** hacia la lista de pedidos.

---

## 📊 Reportes (`/reporte/`)

Template `reporte.html`, que hereda de `base.html`.

| Reporte | Técnica | Modelo |
|---|---|---|
| Total vendido (S/, con `floatformat:2`) | `aggregate()` | `DetallePedido` |
| Pedidos por cliente | `annotate()` | `Cliente` |
| Pedidos por estado | `values().annotate()` | `Pedido` |
| Pedidos del mes, pendientes y entregados | QuerySet personalizado | `Pedido` |
| Consumo total de las recetas | `aggregate()` | `RecetaPizza` |
| Ingredientes y gramos por pizza | `annotate()` | `Pizza` |

---

## 🧩 QuerySets personalizados

| QuerySet | Métodos | Usado en las vistas |
|---|---|---|
| `PedidoQuerySet` | `pendientes()`, `entregados()`, `del_mes()`, `con_detalle()` | `order_list`, `reporte` |
| `PizzaQuerySet` | `disponibles()`, `con_receta()` | `order_create`, `pedido_registrar`, `pizza_list` |

Ambos se asignan con `objects = ...QuerySet.as_manager()` y sus métodos se pueden encadenar, por ejemplo `Pedido.objects.entregados().del_mes()`.

---

## ⚡ Optimización del problema N+1

Medido con `connection.queries` y `reset_queries()` (con `DEBUG=True`):

| Pantalla | Antes | Después | Técnica |
|---|---|---|---|
| Lista de pedidos (`/pedidos/`) | 45 consultas | 3 consultas | `select_related` + `prefetch_related` (`con_detalle()`) |
| Menú de pizzas (`/pizzas/`) | 4 consultas | 2 consultas | `select_related` + `prefetch_related` (`con_receta()`) |

---

## ▶️ Cómo ejecutar

```powershell
cd django_project
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd src
python manage.py migrate
python manage.py runserver
```

- Aplicación: <http://127.0.0.1:8000/>
- Administrador: <http://127.0.0.1:8000/admin/>

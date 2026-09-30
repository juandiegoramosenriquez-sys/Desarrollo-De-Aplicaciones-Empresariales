# 🍕 Semana 06 · Vistas y motor de plantillas

**Curso:** Desarrollo de Aplicaciones Empresariales
**Proyecto:** Pizzería Online (Django 5.2 · SQLite)
**Código:** [`django_project/`](django_project/)

En esta semana la pizzería pasó del Django Admin (uso interno) a páginas públicas construidas con **URL → View → Template**, usando la herencia de plantillas de Django.

---

## 🧱 Herencia de plantillas

| Etiqueta | Qué hace en el proyecto |
|---|---|
| `{% extends 'base.html' %}` | Cada página hereda el molde de `core/templates/base.html` |
| `{% block title %}` / `{% block content %}` | Huecos que cada página rellena con su título y su contenido |
| `{% include %}` | Permite insertar fragmentos reutilizables |

`base.html` aporta a todas las páginas el menú lateral, el footer, Bootstrap 5.3 y Font Awesome (por CDN) y los estilos propios de la pizzería.

---

## 🧩 Sintaxis usada en los templates

- **Variables:** `{{ categoria.nombre }}`
- **Etiquetas de control:** `{% for %}`, `{% if %}`, `{% empty %}`, `{% url %}`
- **Filtros:** `{{ categoria.descripcion|default:'Sin descripción' }}`
- **Mensajes:** alertas de éxito y error con el framework `messages`

---

## 📄 Páginas

Categorías, clientes, datos de entrega, repartidores, métodos de pago, ingredientes, pizzas (menú), recetas, pedidos y detalle de pedido: todas con su CRUD y heredando de `base.html`.

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

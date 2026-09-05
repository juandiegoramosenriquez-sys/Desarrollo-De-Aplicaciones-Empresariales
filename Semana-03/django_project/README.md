# Sistema de Alquiler de Canchas Deportivas

Proyecto desarrollado para el Lab 03 del curso Desarrollo de Aplicaciones Empresariales.

## Problemática

Muchos complejos deportivos manejan sus reservas de canchas de forma manual (llamadas, WhatsApp o cuaderno físico), lo que genera errores como reservas duplicadas o pérdida de información. Los usuarios involucrados son el cliente, que busca reservar una cancha disponible, y el encargado, que administra canchas, horarios y pagos. Se desarrolló una aplicación web que permite al cliente ver la disponibilidad por horario, reservar, y que el encargado gestione el registro de forma centralizada y persistente.

## Requisitos funcionales

1. El sistema debe permitir registrar nuevos clientes.
2. El sistema debe permitir listar los clientes registrados.
3. El sistema debe permitir registrar nuevas sedes.
4. El sistema debe permitir registrar canchas asociadas a un tipo de deporte.
5. El sistema debe permitir listar las canchas disponibles por tipo.
6. El sistema debe permitir crear horarios disponibles para cada cancha.
7. El sistema debe permitir listar los horarios disponibles.
8. El sistema debe permitir a un cliente crear una reserva sobre un horario disponible.
9. El sistema debe permitir listar las reservas realizadas.
10. El sistema debe permitir actualizar el estado de una reserva (pagada/no pagada).
11. El sistema debe permitir eliminar una reserva.
12. El sistema debe marcar un horario como no disponible una vez reservado.

## Modelo de datos

**Entidades independientes:** Cliente, Sede, Cancha
**Entidades relacionadas (ForeignKey):** Horario (FK → Cancha), Reserva (FK → Cliente, FK → Horario)

## App Django

Se creó la app `canchas`, registrada en `INSTALLED_APPS`, con URLs propias enlazadas al proyecto principal mediante `include()`.

## Funcionalidades implementadas (CRUD)

- **CREATE:** formularios de registro para las 5 entidades.
- **READ:** listados con QuerySets (`all()`, `filter()`, `order_by()`) para las 5 entidades.
- **UPDATE:** edición de registros con datos precargados.
- **DELETE:** eliminación con pantalla de confirmación previa.

## Cómo ejecutar el proyecto

```bash
cd src
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Luego entrar a `http://127.0.0.1:8000/`

## Integrantes

- Juan Diego Ramos Enriquez
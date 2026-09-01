# Sistema Empresarial

Aplicación web en Django que gestiona un catálogo simple de ítems.

## Estructura del proyecto

- `src/config/` → configuración del proyecto (settings, urls)
- `src/core/` → aplicación principal (modelos, vistas, plantillas)
- `src/templates/` → plantilla base HTML

## Requisitos

- Python 3.10+
- Django 6

## Instalación y ejecución

1. Clonar el repositorio
2. Crear y activar un entorno virtual:
   \`\`\`
   python -m venv venv
   venv\Scripts\activate
   \`\`\`
3. Instalar dependencias:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`
4. Aplicar migraciones:
   \`\`\`
   cd src
   python manage.py migrate
   \`\`\`
5. Ejecutar el servidor:
   \`\`\`
   python manage.py runserver
   \`\`\`
6. Abrir en el navegador: http://127.0.0.1:8000/
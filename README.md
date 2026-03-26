# EcoStock Sim (Django)

Simulación académica inspirada en una plataforma de inventario para que puedas correrla con **Python + Django** y usarla en pruebas de seguridad y calidad.

## Requisitos
- Python 3.10 o superior
- pip

## Instalación
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

## Accesos demo
- Usuario: `admin`
- Contraseña: `admin123`

## Módulos incluidos
- Login
- Recuperar contraseña simulada
- Dashboard
- CRUD de productos
- Admin de Django

## URLs principales
- `/login/`
- `/`
- `/productos/`
- `/admin/`

## Para tu reporte de seguridad
Te sirve para documentar:
- validación de formularios
- control de acceso por login
- protección CSRF
- manejo de sesiones
- pruebas CRUD
- errores 404 y 500 controlados

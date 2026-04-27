# PW2-2026-Flask

Proyecto de ejemplo usando Flask y Flask-WTF para manejo de formularios seguros, validaciones, autenticación básica y gestión de avatares con imágenes.

## Requisitos previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación y configuración

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/dperezalvarez/PW2-2026-Flask.git
   cd PW2-2026-Flask
   ```

2. **Crea un entorno virtual:**
   ```bash
   python3 -m venv venv
   # En Linux/Mac
   source venv/bin/activate
   # En Windows
   venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

   Esto instalará:
   - Flask
   - Flask-WTF
   - email-validator
   - (otras dependencias necesarias)

## Estructura del proyecto

```
PW2-2026-Flask/
│   app.py
│   requirements.txt
│   extensions.py
│   forms.py
│   models.py
│
├── routes/
│     __init__.py
│     auth.py
│     main.py
│
├── static/
│   ├── css/
│   │     style.css
│   └── avatars/   # Carpeta sugerida para almacenar imágenes de avatar
│
└── templates/
    base.html
    index.html
    login.html
    register.html
    create_user.html
    edit_user.html
```

- **app.py**: Punto de entrada de la aplicación Flask.
- **requirements.txt**: Lista de dependencias del proyecto.
- **forms.py**: Definición de formularios WTForms.
- **models.py**: Modelos de datos (si aplica).
- **routes/**: Rutas y controladores de la app.
- **templates/**: Plantillas HTML para las vistas.
- **static/**: Archivos estáticos (CSS, imágenes, JS).
- **static/avatars/**: Carpeta para almacenar imágenes de avatar de usuario.

## Ejecución de la aplicación

1. Asegúrate de tener el entorno virtual activado.
2. Ejecuta la aplicación:
   ```bash
   flask run
   ```
   o
   ```bash
   python app.py
   ```
3. Accede a `http://127.0.0.1:5000` en tu navegador.

## Funcionalidades principales
- Formularios seguros con Flask-WTF y validaciones personalizadas (mensajes en español).
- Autenticación de usuarios y rutas protegidas.
- Plantillas adaptadas para mostrar errores y proteger contra CSRF automáticamente.
- Gestión de avatar de usuario: permite subir y mostrar imágenes de perfil (avatar) usando Flask. Las imágenes se almacenan en el servidor y se muestran en las vistas de usuario.

## Notas adicionales
- Para la funcionalidad de avatar, asegúrate de tener una carpeta para almacenar imágenes (por ejemplo, `static/avatars/`).
- Recuerda configurar la variable de entorno `FLASK_APP=app.py` si usas `flask run`.
- Puedes modificar las plantillas en la carpeta `templates/` para personalizar la interfaz.
- Para agregar nuevas dependencias, usa `pip install <paquete>` y luego `pip freeze > requirements.txt`.

---

¡Listo! Sigue estos pasos para levantar y trabajar con el proyecto.

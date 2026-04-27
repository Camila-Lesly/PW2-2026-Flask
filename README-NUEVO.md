# PW2-2026-Flask

Proyecto de ejemplo con Flask, autenticación, formularios seguros y gestión de avatares.

## Requisitos
- Python 3.8+
- pip

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/dperezalvarez/PW2-2026-Flask.git
   cd PW2-2026-Flask
   ```
2. Crea un entorno virtual y actívalo:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

1. Asegúrate de tener la carpeta `static/avatars/` creada (ya incluida en el repo).
2. Ejecuta:
   ```bash
   flask run
   ```
   o
   ```bash
   python app.py
   ```
3. Abre tu navegador en: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Características
- Registro y login de usuarios.
- Subida de imagen de perfil (avatar) opcional.
- Si no hay imagen, se muestra un círculo con la inicial del nombre.
- Formularios protegidos con CSRF y validaciones.
- Vistas con Bootstrap y herencia de plantillas.

## Estructura básica

```
PW2-2026-Flask/
│   app.py
│   requirements.txt
│   forms.py
│   models.py
│   extensions.py
│
├── routes/
│     auth.py
│     main.py
│     __init__.py
│
├── templates/
│     base.html
│     index.html
│     login.html
│     register.html
│     create_user.html
│     edit_user.html
│
└── static/
    ├── css/
    │     style.css
    └── avatars/
```

## Notas
- Puedes modificar las plantillas en `templates/` para personalizar la interfaz.
- Si agregas dependencias, ejecuta `pip freeze > requirements.txt`.
- Para desarrollo, usa `debug=True` en `app.py`.

---

¡Listo! Sigue estos pasos para levantar y probar el proyecto.

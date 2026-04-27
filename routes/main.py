from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from routes.auth import users_db

main = Blueprint('main', __name__)


usuarios = [
    {'nombre': 'Ana López', 'email': 'ana@ejemplo.com', 'avatar': None},
    {'nombre': 'Carlos García', 'email': 'carlos@ejemplo.com', 'avatar': None},
    {'nombre': 'María Pérez', 'email': 'maria@ejemplo.com', 'avatar': None}
]

@main.route('/')
def inicio():
    # Combinar usuarios ficticios y registrados
    usuarios_registrados = []
    for user in users_db.values():
        usuarios_registrados.append({
            'nombre': getattr(user, 'username', None),
            'email': user.email,
            'avatar': getattr(user, 'avatar', None)
        })
    todos = usuarios + usuarios_registrados
    return render_template('index.html', usuarios=todos)

@main.route('/contacto', methods=['GET', 'POST'])
@login_required
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        
        if nombre and email:
            nuevo_usuario = {'nombre': nombre, 'email': email}
            usuarios.append(nuevo_usuario)
            flash(f'¡Gracias {nombre}! Te contactaremos en {email}')
            return redirect(url_for('main.inicio'))
        else:
            flash('Por favor completa todos los campos')
    
    return render_template('contacto.html')

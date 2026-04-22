from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required

main = Blueprint('main', __name__)

usuarios = [
    {'nombre': 'Ana López', 'email': 'ana@ejemplo.com'},
    {'nombre': 'Carlos García', 'email': 'carlos@ejemplo.com'},
    {'nombre': 'María Pérez', 'email': 'maria@ejemplo.com'}
]

@main.route('/')
def inicio():
    return render_template('index.html', usuarios=usuarios)

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

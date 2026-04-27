from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import UserMixin, login_user, logout_user, login_required
from werkzeug.utils import secure_filename
import os
from forms import RegisterForm

auth = Blueprint('auth', __name__)


# Clase de usuario simple compatible con Flask-Login (ahora con avatar)
class User(UserMixin):
    def __init__(self, id, username, email, password, avatar=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.avatar = avatar

# Base de datos ficticia de usuarios
users_db = {
    '1': User('1', 'admin', 'admin@ejemplo.com', '1234', avatar=None)
}
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        avatar_file = form.avatar.data

        # Verificar si el email ya existe
        if any(u.email == email for u in users_db.values()):
            flash('El correo ya está registrado', 'danger')
            return render_template('register.html', form=form)

        # Guardar avatar si se subió
        avatar_filename = None
        if avatar_file:
            filename = secure_filename(avatar_file.filename)
            avatar_path = os.path.join('static', 'avatars')
            os.makedirs(avatar_path, exist_ok=True)
            avatar_filename = f"{username}_{filename}"
            avatar_file.save(os.path.join(avatar_path, avatar_filename))

        # Crear nuevo usuario
        new_id = str(len(users_db) + 1)
        user = User(new_id, username, email, password, avatar=avatar_filename)
        users_db[new_id] = user
        flash('Usuario registrado exitosamente. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validación simple
        user = next((u for u in users_db.values() if u.email == email), None)
        
        if user and user.password == password:
            login_user(user)
            flash('¡Sesión iniciada con éxito!')
            return redirect(url_for('main.inicio'))
        else:
            flash('Email o contraseña incorrectos', 'danger')
            
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión')
    return redirect(url_for('main.inicio'))

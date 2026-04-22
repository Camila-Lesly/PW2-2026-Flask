from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import UserMixin, login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

# Clase de usuario simple compatible con Flask-Login
class User(UserMixin):
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

# Base de datos ficticia de usuarios
users_db = {
    '1': User('1', 'admin@ejemplo.com', '1234')
}

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

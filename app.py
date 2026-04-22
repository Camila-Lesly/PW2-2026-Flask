from flask import Flask
from flask_login import LoginManager
from routes.main import main
from routes.auth import auth, users_db

app = Flask(__name__)
app.secret_key = '1234'  # Necesario para sesiones y flash

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Ruta a la que redirigir si se requiere login
login_manager.login_message = "Por favor, inicia sesión para acceder a esta página."
login_manager.login_message_category = "info"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return users_db.get(user_id)

# Registro de Blueprints
app.register_blueprint(main)
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger  # Importa o Swagger
from config import Config
from models import db
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar o SQLAlchemy
db.init_app(app)

# Inicializar o JWTManager
jwt = JWTManager(app)

# Inicializar o Swagger
swagger = Swagger(app)

# Registrar blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

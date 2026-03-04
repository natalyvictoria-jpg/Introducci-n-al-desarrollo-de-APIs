from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .config import DevelopmentConfig

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # Inicializar extensiones
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Registrar blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    from .routes.estudiante_routes import estudiante_bp
    app.register_blueprint(estudiante_bp)

    from .routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
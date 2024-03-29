import os
from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Inicializar la extensión SQLAlchemy
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    # Configuración de la base de datos PostgreSQL.
    db_parameters = {
        "user": os.getenv('DB_USER'),
        "password": os.getenv('DB_PASSWORD'),
        "host": os.getenv('DB_HOST', 'localhost'),
        "port": os.getenv('DB_PORT', '5433'),
        "dbname": os.getenv('DB_NAME')
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI').format(**db_parameters)

    # Inicializar la extensión SQLAlchemy con la aplicación Flask
    db.init_app(app)
    
    
    # Inicializar la extensión Flask-Migrate
    migrate = Migrate(app, db)
    migrate.init_app(app,db)

    # Importar y registrar los controladores de las rutas 
    from app.controllers import user  
    app.register_blueprint(user, url_prefix='/user')
    # Contexto del shell para interactuar con la aplicación durante el shell interactivo
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app

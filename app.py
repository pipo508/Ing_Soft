import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Configuración de las variables de entorno de la base de datos
    db_user = os.getenv('DB_USER', 'postgres')
    db_password = os.getenv('DB_PASSWORD', 'Tiziano756')
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = os.getenv('DB_PORT', '5432')  # Se proporciona un valor predeterminado
    db_name = os.getenv('DB_NAME', 'ing_soft')
    
    # Configuración de la URL de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    db.init_app(app)  # Inicializa SQLAlchemy con la aplicación Flask

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=True)

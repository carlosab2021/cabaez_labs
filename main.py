from flask import Flask
from app.app_porcentaje import app_porcentaje
from app.app_genero import app_genero
from app.app_genero_horas import app_genero_horas
from app.app_desarrollador import app_desarrollador
from app.app_userdata import app_userdata

app = Flask(__name__)

# Registra las rutas para cada aplicación
app.register_blueprint(app_porcentaje, url_prefix='/porcentaje')
app.register_blueprint(app_genero, url_prefix='/genero')
app.register_blueprint(app_genero_horas, url_prefix='/genero_horas')
app.register_blueprint(app_desarrollador, url_prefix='/desarrollador')
app.register_blueprint(app_userdata, url_prefix='/user_data')


if __name__ == '__main__':
    app.run(debug=True)

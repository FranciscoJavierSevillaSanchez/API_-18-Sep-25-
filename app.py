import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv 

#Cargar las variables de entorno
load_dotenv()

#crear instancia
app =  Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Modelo de la base de datos
class Alumno(db.Model):
    __tablename__ = 'alumnos'
    no_control = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String)
    ap_paterno = db.Column(db.String)
    ap_materno = db.Column(db.String)
    semestre = db.Column(db.Integer)

# Crear las tablas si no existen
with app.app_context():
    db.create_all()
    
#endpoint para obtener todos los alumnos
@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    alumnos = Alumno.query.all()
    lista_alumnos = []
    for alumno in alumnos:
        lista_alumnos.append({
            'no_control ': alumno.no_control,
            'nombre ': alumno.nombre,
            'ap_paterno ': alumno.ap_paterno,
            'ap_materno ': alumno.ap_materno,
            'semestre ': alumno.semestre
        })
    return jsonify(lista_alumnos)


if __name__ == ('__main__'):
    app.run(debug=True)
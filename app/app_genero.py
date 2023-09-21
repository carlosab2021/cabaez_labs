from flask import Flask, Blueprint, request, jsonify
import pandas as pd

# creamos la API, sobre busqueda de generos
# Cargar el archivo CSV
app_genero = Blueprint('app_genero', __name__)
df = pd.read_csv('resultado_union_actualizado.csv')

import unicodedata

import json

# ...

@app_genero.route('/buscar_genero', methods=['GET'])
def buscar_genero():
    genero_a_buscar = request.args.get('genero')

    if not genero_a_buscar:
        return jsonify({"error": "Por favor, proporcione un género para buscar."})

    # Crear un DataFrame que contenga solo las filas con el género especificado
    genero_df = df[df['genres'].str.contains(genero_a_buscar, case=False, na=False)]

    # Calcular el ranking de acuerdo a 'playtime_forever' para el género especificado
    genero_df.loc[:, 'rank'] = genero_df['playtime_forever'].rank(ascending=False, method='min')

    # Mostrar el ranking del género especificado
    if genero_df.empty:
        return jsonify({"message": f"El género '{genero_a_buscar}' no se encuentra en el dataset."})
    else:
        ranking = genero_df['rank'].iloc[0]
        
        # Crear un diccionario con el mensaje y serializarlo con json.dumps
        mensaje = {"message": f"El género '{genero_a_buscar}' está en el puesto {int(ranking)} en el ranking de acuerdo a 'playtime_forever'."}
        mensaje_json = json.dumps(mensaje, ensure_ascii=False).encode('utf8')
        
        return mensaje_json, 200, {'Content-Type': 'application/json; charset=utf-8'}

        
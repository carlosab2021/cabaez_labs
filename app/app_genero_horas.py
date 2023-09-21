from flask import Flask, Blueprint, request, jsonify
import pandas as pd

app_genero_horas = Blueprint('app_genero_horas', __name__)
df = pd.read_csv('resultado_union_actualizado.csv')

# Función para obtener los mejores usuarios en un género dado
def userforgenre(genero):
    # Cargar el archivo CSV en un DataFrame
    
    # Tratar los valores faltantes en la columna 'genres'
    df['genres'] = df['genres'].fillna('')  # Reemplaza los NaN con una cadena vacía

    # Filtrar las filas que corresponden al género dado en la columna 'genres'
    df_genero = df[df['genres'].str.contains(genero)]

    # Ordenar el DataFrame por horas de juego en orden descendente
    df_genero_sorted = df_genero.sort_values(by='playtime_forever', ascending=False)

    # Tomar los 5 primeros usuarios
    top_5_usuarios = df_genero_sorted.head(5)

    # Obtener una lista de diccionarios con la información requerida
    resultado = top_5_usuarios[['user_id', 'url', 'playtime_forever']].to_dict(orient='records')

    return resultado

# Ruta para obtener los mejores usuarios en un género dado
@app_genero_horas.route('/mejores_usuarios_por_genero', methods=['GET'])
def obtener_mejores_usuarios_por_genero():
    genero = request.args.get('genero')

    if not genero:
        return jsonify({"error": "Por favor, proporcione un género para buscar."})

    top_usuarios = userforgenre(genero)

    return jsonify({"top_usuarios": top_usuarios})


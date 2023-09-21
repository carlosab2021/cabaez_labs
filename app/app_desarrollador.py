from flask import Flask, Blueprint, request, jsonify
import pandas as pd
import numpy as np

app_desarrollador = Blueprint('app_desarrollador', __name__)

# Función para obtener el resumen de un desarrollador
def developer(desarrollador):
    try:
        # Cargar el archivo CSV en un DataFrame
        df = pd.read_csv('resultado_sin_nulos.csv')

        # Filtrar las filas que corresponden al desarrollador dado
        df_desarrollador = df[df['developer'] == desarrollador].copy()  # Añadir .copy() para evitar la advertencia

        # Extraer el año de la columna 'release_date'
        df_desarrollador['year'] = pd.to_datetime(df_desarrollador['release_date']).dt.year

        # Contar la cantidad de juegos "Free to Play" por año
        cantidad_free_to_play = df_desarrollador[df_desarrollador['price'] == 'Free to Play'].groupby('year')['item_id'].count()

        # Contar la cantidad total de items por año
        cantidad_total_items = df_desarrollador.groupby('year')['item_id'].count()

        # Calcular el porcentaje de contenido gratuito por año (manejo de valores nulos y formas)
        porcentaje_free_to_play = calculate_percentage(cantidad_free_to_play, cantidad_total_items)

        # Crear un DataFrame con los resultados
        resultados = pd.DataFrame({
            'Year': cantidad_free_to_play.index,
            'Cantidad de Free to Play': cantidad_free_to_play.values,
            'Cantidad Total de Items': cantidad_total_items.values,
            'Porcentaje de Contenido Gratuito': porcentaje_free_to_play
        })

        return resultados.to_dict(orient='records')

    except Exception as e:
        return {"error": str(e)}

# Función para calcular el porcentaje de contenido gratuito por año (manejo de valores nulos y formas)
def calculate_percentage(free_to_play, total_items):
    if len(free_to_play) == 0 or len(total_items) == 0:
        return np.zeros_like(total_items)  # Si uno de los arreglos está vacío, retorna ceros
    
    return np.divide(free_to_play, total_items, out=np.zeros_like(total_items), where=total_items != 0) * 100

# Ruta para obtener el resumen de un desarrollador
@app_desarrollador.route('/resumen_desarrollador', methods=['GET'])
def obtener_resumen_desarrollador():
    desarrollador = request.args.get('desarrollador')

    if not desarrollador:
        return jsonify({"error": "Por favor, proporcione un nombre de desarrollador para buscar."})

    resumen = developer(desarrollador)

    return jsonify({"resumen": resumen})





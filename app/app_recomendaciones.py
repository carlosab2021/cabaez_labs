from flask import Flask, Blueprint, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app_recomendaciones = Blueprint('app_recomendaciones', __name__)

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('resultado_union_actualizado.csv')

# Seleccionar las columnas relevantes para el cálculo de similitud
df = df[['user_id', 'item_id', 'genres', 'review']]

# Preprocesamiento de datos
# Combinar la información de géneros y reseñas en una sola columna
df['features'] = df['genres'] + ' ' + df['review']

# Crear una matriz TF-IDF para representar las características de los juegos
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['features'].fillna(''))

# Calcular la similitud del coseno entre los juegos
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Función para obtener recomendaciones de juegos similares
def get_recommendations(item_id, cosine_sim=cosine_sim):
    idx = df[df['item_id'] == item_id].index
    if len(idx) > 0:
        idx = idx[0]  # Tomar el primer índice encontrado

        sim_scores = list(enumerate(cosine_sim[idx]))

        # Filtrar el juego de entrada antes de ordenar las puntuaciones de similitud
        sim_scores = [x for x in sim_scores if x[0] != idx]

        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        sim_scores = sim_scores[:10]  # Obtén las 10 mejores recomendaciones
        game_indices = [i[0] for i in sim_scores]

        return df['item_id'].iloc[game_indices]
    else:
        return []

# Ruta para obtener recomendaciones de juegos similares
@app_recomendaciones.route('/recomendar_juegos', methods=['GET'])
def obtener_recomendaciones_juegos():
    item_id = request.args.get('item_id')

    if not item_id:
        return jsonify({"error": "Por favor, proporcione un item_id para obtener recomendaciones."})

    recommendations = get_recommendations(float(item_id))

    if not recommendations.empty:  # Verificar si la Serie no está vacía
        return jsonify({"recommendations": recommendations.tolist()})
    else:
        return jsonify({"message": "No se encontraron recomendaciones para el juego proporcionado."})









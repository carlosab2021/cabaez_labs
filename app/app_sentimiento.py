# En app_sentimiento.py
from flask import Flask, Blueprint, request, jsonify
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app_sentimiento = Blueprint('app_sentimiento', __name__)
df = pd.read_csv('resultado_union_actualizado.csv')

# Descargar el recurso de NLTK si aún no está descargado
nltk.download('vader_lexicon')

# Función para realizar análisis de sentimiento para un año dado
def sentiment_analysis(año):
    # Cargar el archivo CSV en un DataFrame y convertir la columna 'fecha_convertida' a datetime
    df = pd.read_csv('resultado_union_actualizado.csv', parse_dates=['fecha_convertida'])

    # Filtrar las reseñas para el año especificado
    df_filtrado = df[df['fecha_convertida'].dt.year == año]

    # Eliminar filas con valores NaN en la columna 'review'
    df_filtrado = df_filtrado.dropna(subset=['review'])

    # Inicializar el analizador de sentimiento VADER
    sia = SentimentIntensityAnalyzer()

    # Inicializar un contador para cada categoría de sentimiento
    sentiment_counts = {'Negative': 0, 'Neutral': 0, 'Positive': 0}

    # Realizar el análisis de sentimiento para cada reseña
    for index, row in df_filtrado.iterrows():
        review = row['review']
        sentiment = sia.polarity_scores(review)
        
        # Determinar la categoría de sentimiento y actualizar el contador
        if sentiment['compound'] >= 0.05:
            sentiment_counts['Positive'] += 1
        elif sentiment['compound'] <= -0.05:
            sentiment_counts['Negative'] += 1
        else:
            sentiment_counts['Neutral'] += 1

    return sentiment_counts

# Ruta para obtener los resultados del análisis de sentimiento para un año dado
@app_sentimiento.route('/analisis_sentimiento', methods=['GET'])
def obtener_analisis_sentimiento():
    año = request.args.get('año')

    if not año:
        return jsonify({"error": "Por favor, proporcione un año para analizar el sentimiento."})

    resultados = sentiment_analysis(int(año))

    return jsonify({"resultados": resultados})

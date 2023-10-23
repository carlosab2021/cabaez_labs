from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Carga la base de datos con análisis de sentimiento desde el archivo CSV
data = pd.read_csv('base_de_datos_con_sentimiento.csv')

# Ruta para obtener el análisis de sentimiento según el año de lanzamiento
@app.get('/sentiment_analysis/{ano}')
async def sentiment_analysis(ano: int):
    # Filtra los datos para el año especificado
    filtered_data = data[data['fecha_convertida'].str.contains(str(ano))]

    if filtered_data.empty:
        raise HTTPException(status_code=404, detail="No se encontraron datos para el año especificado.")

    # Realiza el recuento de análisis de sentimiento
    sentiment_counts = filtered_data['sentiment'].value_counts()

    # Convierte el resultado a un diccionario
    result = sentiment_counts.to_dict()

    return result


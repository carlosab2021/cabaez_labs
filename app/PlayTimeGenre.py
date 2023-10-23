from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Carga la base de datos desde el archivo CSV
data = pd.read_csv('resultado_union_actualizado.csv')

# Ruta para obtener el año con más horas jugadas para un género dado
@app.get('/PlayTimeGenre/{genero}')
async def playtime_genre(genero: str):
    genero = genero.strip('[]').strip("'")  # Elimina los corchetes para obtener el género real
    filtered_data = data[data['genres'].str.contains(genero, case=False, na=False)]

    if filtered_data.empty:
        raise HTTPException(status_code=404, detail="No se encontraron datos para el género especificado.")

    max_horas = filtered_data['playtime_forever'].max()
    año_max_horas = filtered_data[filtered_data['playtime_forever'] == max_horas]['fecha_convertida'].values[0]

    return {"Año de lanzamiento con más horas jugadas para " + genero: año_max_horas}


from fastapi import FastAPI, Query

app_genero = FastAPI()
import pandas as pd
import unicodedata
import json

# Cargar el archivo CSV
df = pd.read_csv('resultado_union_actualizado.csv')

# Ruta para buscar un género
@app_genero.get('/buscar_genero')
async def buscar_genero(genero: str = Query(..., description="Género a buscar")):
    try:
        # Crear un DataFrame que contenga solo las filas con el género especificado
        genero_df = df[df['genres'].str.contains(genero, case=False, na=False)]

        # Calcular el ranking de acuerdo a 'playtime_forever' para el género especificado
        genero_df.loc[:, 'rank'] = genero_df['playtime_forever'].rank(ascending=False, method='min')

        # Mostrar el ranking del género especificado
        if genero_df.empty:
            return {"message": f"El género '{genero}' no se encuentra en el dataset."}
        else:
            ranking = genero_df['rank'].iloc[0]

            # Crear un diccionario con el mensaje
            mensaje = {"message": f"El género '{genero}' está en el puesto {int(ranking)} en el ranking de acuerdo a 'playtime_forever'."}

            return mensaje
    except Exception as e:
        return {"error": str(e)}

from fastapi import FastAPI, Query

app_genero_horas = FastAPI()

import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('resultado_union_actualizado.csv')

# Función para obtener los mejores usuarios en un género dado
def userforgenre(genero):
    try:
        # Tratar los valores faltantes en la columna 'genres'
        df['genres'] = df['genres'].fillna('')  # Reemplaza los NaN con una cadena vacía

        # Filtrar las filas que corresponden al género dado en la columna 'genres'
        df_genero = df[df['genres'].str.contains(genero, case=False, na=False)]

        # Ordenar el DataFrame por horas de juego en orden descendente
        df_genero_sorted = df_genero.sort_values(by='playtime_forever', ascending=False)

        # Tomar los 5 primeros usuarios
        top_5_usuarios = df_genero_sorted.head(5)

        # Obtener una lista de diccionarios con la información requerida
        resultado = top_5_usuarios[['user_id', 'url', 'playtime_forever']].to_dict(orient='records')

        return resultado
    except Exception as e:
        return {"error": str(e)}

# Ruta para obtener los mejores usuarios en un género dado
@app_genero_horas.get('/mejores_usuarios_por_genero')
def obtener_mejores_usuarios_por_genero(genero: str = Query(..., description="Género a buscar")):
    top_usuarios = userforgenre(genero)
    return {"top_usuarios": top_usuarios}



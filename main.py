<<<<<<< HEAD
from fastapi import FastAPI
from app.PlayTimeGenre import app as PlayTimeGenre
from app.sentiment_analysis import app as SentimentAnalysis
from app.UserForGenre import app as UserForGenre
from app.UsersNotRecommend import app as UsersNotRecommend
from app.UsersRecommend import app as UsersRecommend

app = FastAPI()

# Monta las subaplicaciones FastAPI en sus rutas respectivas
main_app.mount("/PlayTimeGenre", PlayTimeGenre)
main_app.mount("/sentiment_analysis", SentimentAnalysis)
main_app.mount("/UserForGenre", UserForGenre)
main_app.mount("/UsersNotRecommend", UsersNotRecommend)
main_app.mount("/UsersRecommend", UsersRecommend)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)

=======
from fastapi import FastAPI, HTTPException, Request
import pandas as pd
from prettytable import PrettyTable
from fastapi.responses import JSONResponse
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Cargar el DataFrame desde el archivo CSV para la API calcular_porcentaje_y_cantidad
df_calculo = pd.read_csv('usuario_reviews_sinfechas_nulos.csv')
>>>>>>> b4d04da9da9b6950ac58f827e5115f7b7ff151ae

# Cargar el DataFrame desde el archivo CSV para las otras APIs (buscar_genero y userdata)
df_buscar_genero = pd.read_csv('resultado_union_actualizado.csv')
df_userdata = pd.read_csv('resultado_sin_nulos.csv')

# Cargar los DataFrames desde los archivos CSV adicionales
df_reviews = pd.read_csv('usuario_reviews_sinfechas_nulos.csv')
df_games = pd.read_csv('resultado_union_actualizado.csv')
df_users_items = pd.read_csv('resultado_union_actualizado.csv')
# Define las fechas mínimas y máximas permitidas fuera de la función
fecha_minima = pd.to_datetime('2011-01-01')
fecha_maxima = pd.to_datetime('2016-12-31')

@app.route('/calcular_porcentaje_y_cantidad', methods=['GET'])
def calcular_porcentaje_y_cantidad_api(request: Request):
    fecha_ini = request.query_params.get('fecha_ini')
    fecha_fin = request.query_params.get('fecha_fin')
    
    try:
        fecha_ini = pd.to_datetime(fecha_ini, errors='coerce')
        fecha_fin = pd.to_datetime(fecha_fin, errors='coerce')
        
        # Valida que las fechas estén dentro del rango permitido
        if fecha_ini < fecha_minima or fecha_fin > fecha_maxima:
            raise HTTPException(status_code=400, detail="Las fechas están fuera del rango permitido")
        
        df_calculo['fecha_convertida'] = pd.to_datetime(df_calculo['fecha_convertida'], errors='coerce')
        
        df_filtrado = df_calculo[(df_calculo['fecha_convertida'] >= fecha_ini) & (df_calculo['fecha_convertida'] <= fecha_fin)]
        
        cantidad_usuarios = df_filtrado['user_id'].nunique()
        porcentaje_recomendacion = (df_filtrado['recommend'].sum() / len(df_filtrado)) * 100
        
        resultado = {
            'fecha_ini': fecha_ini.strftime('%Y-%m-%d'),
            'fecha_fin': fecha_fin.strftime('%Y-%m-%d'),
            'cantidad_usuarios': cantidad_usuarios,
            'porcentaje_recomendacion': porcentaje_recomendacion
        }
        
        # Crear una tabla con los resultados
        tabla_resultado = PrettyTable()
        tabla_resultado.field_names = ['Campo', 'Valor']
        
        for campo, valor in resultado.items():
            tabla_resultado.add_row([campo, valor])
        
        return JSONResponse(content=str(tabla_resultado))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@app.get("/buscar_genero/")
def buscar_genero(genero: str):
    try:
        # Lógica para buscar el género en el DataFrame df_buscar_genero
        genero_df = df_buscar_genero[df_buscar_genero['genres'].str.contains(genero, case=False, na=False)]

        if genero_df.empty:
            raise HTTPException(status_code=404, detail=f"El género '{genero}' no se encuentra en el dataset.")

        ranking = genero_df['playtime_forever'].rank(ascending=False, method='min').iloc[0]
        return {"message": f"El género '{genero}' está en el puesto {int(ranking)} en el ranking de acuerdo a 'playtime_forever'."}
    except Exception as e:
        # Registrar el error
        print(f"Error en buscar_genero: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@app.get("/userdata/{user_id}")
def userdata(user_id: str):
    try:
        # Lógica para obtener los datos del usuario en el DataFrame df_userdata
        user_data = df_userdata[df_userdata['user_id'] == user_id]
        
        if user_data.empty:
            raise HTTPException(status_code=404, detail=f"Usuario '{user_id}' no encontrado en el dataset.")
        
        # Realizar aquí las operaciones necesarias con los datos del usuario
        
        return JSONResponse(content={"message": "Datos del usuario aquí"})
    except Exception as e:
        # Registrar el error
        print(f"Error en userdata: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@app.route('/userdata', methods=['GET'])
def userdata_api(request: Request):
    user_id = request.query_params.get('User_id')

    try:
        # Filtrar las reviews para el usuario específico
        user_reviews = df_reviews[df_reviews['user_id'] == user_id]

        # Calcular la cantidad de dinero gastado por el usuario
        dinero_gastado = user_reviews['precio'].sum()  # Asumiendo que hay una columna 'precio' en las reviews

        # Calcular el porcentaje de recomendación basado en las reviews
        total_reviews = len(user_reviews)
        if total_reviews == 0:
            porcentaje_recomendacion = 0
        else:
            porcentaje_recomendacion = (user_reviews['recommend'].sum() / total_reviews) * 100

        # Calcular la cantidad de items del usuario
        cantidad_items = len(user_reviews)

        resultado = {
            'user_id': user_id,
            'dinero_gastado': dinero_gastado,
            'porcentaje_recomendacion': porcentaje_recomendacion,
            'cantidad_items': cantidad_items
        }

        return JSONResponse(content=resultado)

    except Exception as e:
        return JSONResponse(content={'error': str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)


from fastapi import FastAPI, Query

app_porcentaje = FastAPI()
import pandas as pd

# DataFrame desde el archivo CSV
df = pd.read_csv('usuario_reviews_sinfechas_nulos.csv')

# Definimos las fechas mínimas y máximas permitidas acorde a mi base de datos
fecha_minima = pd.to_datetime('2011-01-01')
fecha_maxima = pd.to_datetime('2016-12-31')

@app_porcentaje.get('/calcular_porcentaje_y_cantidad')  # Cambio aquí
async def calcular_porcentaje_y_cantidad_api(fecha_ini: str = Query(..., description="Fecha de inicio"),
                                             fecha_fin: str = Query(..., description="Fecha de fin")):
    try:
        fecha_ini = pd.to_datetime(fecha_ini, errors='coerce')
        fecha_fin = pd.to_datetime(fecha_fin, errors='coerce')
        
        # Valida que las fechas estén dentro del rango permitido
        if fecha_ini < fecha_minima or fecha_fin > fecha_maxima:
            return {"error": "Las fechas están fuera del rango permitido"}
        
        df['fecha_convertida'] = pd.to_datetime(df['fecha_convertida'], errors='coerce')
        
        df_filtrado = df[(df['fecha_convertida'] >= fecha_ini) & (df['fecha_convertida'] <= fecha_fin)]
        
        cantidad_usuarios = df_filtrado['user_id'].nunique()
        porcentaje_recomendacion = (df_filtrado['recommend'].sum() / len(df_filtrado)) * 100
        
        resultado = {
            'fecha_ini': fecha_ini.strftime('%Y-%m-%d'),
            'fecha_fin': fecha_fin.strftime('%Y-%m-%d'),
            'cantidad_usuarios': cantidad_usuarios,
            'porcentaje_recomendacion': porcentaje_recomendacion
        }
        
        return resultado
    
    except Exception as e:
        return {'error': str(e)}



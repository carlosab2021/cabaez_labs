from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv('resultado_union_actualizado.csv')
@app.get("/buscar_genero/")
def buscar_genero(genero: str):
    # Lógica para buscar el género en el DataFrame
    genero_df = df[df['genres'].str.contains(genero, case=False, na=False)]

    if genero_df.empty:
        return {"message": f"El género '{genero}' no se encuentra en el dataset."}
    else:
        ranking = genero_df['playtime_forever'].rank(ascending=False, method='min').iloc[0]
        return {"message": f"El género '{genero}' está en el puesto {int(ranking)} en el ranking de acuerdo a 'playtime_forever'."}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)

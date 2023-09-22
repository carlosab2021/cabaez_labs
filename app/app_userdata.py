from flask import Blueprint, request, jsonify
import pandas as pd
app_userdata = Blueprint('app_userdata', __name__)

# Cargar los datos desde el archivo CSV
df = pd.read_csv('resultado_union_actualizado.csv')

def userdata(User_id: str):
    # Lista de términos a buscar en la columna 'tags'
    terminos_a_buscar = ['FPS', 'Zombies', 'Co-op', 'Survival', 'Action', 'Multiplayer', 'Horror', 'Online Co-Op', 'Shooter', 'Gore', 'Team-Based', 'First-Person', 'Moddable', 'Survival Horror', 'Great Soundtrack', 'Singleplayer', 'Class-Based', 'Difficult', 'Comedy', 'Adventure']

    # Crear una serie de valores booleanos para cada término
    condiciones = [df['tags'].str.contains(termino) for termino in terminos_a_buscar]

    # Combinar las condiciones utilizando 'or' para buscar cualquier término
    condicion_final = any(condicion.any() for condicion in condiciones)

    # Filtrar las compras del usuario específico que contienen al menos uno de los términos
    user_purchases = df[(df['user_id'] == User_id) & condicion_final]

    # Calcular la cantidad de dinero gastado por el usuario
    total_spent = user_purchases['price'].sum()

    # Calcular el porcentaje de recomendación en base a reviews.recommend
    user_reviews = df[df['user_id'] == User_id]
    recommendation_percentage = user_reviews['recommend'].mean() * 100

    # Calcular la cantidad de items
    num_items = len(user_purchases)

    return {
        "total_spent": total_spent,
        "recommendation_percentage": recommendation_percentage,
        "num_items": num_items
    }

@app_userdata.route('/user_data', methods=['GET'])
def get_user_data():
    User_id = request.args.get('user_id')
    if User_id:
        data = userdata(User_id)
        return jsonify(data)
    else:
        return jsonify({"error": "User_id parameter is required."}), 400

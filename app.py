# Importar las librerías necesarias
# Importar flask para crear la API
from flask import Flask,request, url_for, redirect, render_template, jsonify
# Importar las funciones de pycaret para cargar el modelo y hacer predicciones
from pycaret.regression import *
# Importar pandas para manejar los datos
import pandas as pd
# Importar pickle para cargar el modelo guardado
import pickle
# Importar numpy para manejar arrays
import numpy as np

# app es la instancia de Flask que se usará para crear la API
app = Flask(__name__)

# Cargar el modelo previamente guardado
model = load_model('deployment_20231111')
# Definir las columnas que se usarán para las predicciones
cols = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

# Definir la ruta principal de la aplicación
@app.route('/')
def home():
    return render_template("home.html")

# Definir la ruta para verificar la salud de la API
@app.route('/health', methods=["GET"])
def health():
    return "HEALTH OK"

# Definir la ruta para hacer predicciones
@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen, round = 0)
    print(prediction)
    prediction = int(prediction.loc[0, 'prediction_label'])
    return render_template('home.html',pred='Expected Bill will be ${} anually'.format(prediction))

# Definir la ruta para hacer predicciones a través de una API
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = predict_model(model, data=data_unseen)
    output = prediction.Label[0]
    return jsonify(output)

# Definir la ruta para hacer predicciones a través de un archivo CSV
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# Importar las librerías necesarias
from flask import Flask, request, render_template, jsonify
from pycaret.regression import load_model, predict_model
import pandas as pd
import numpy as np

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Cargar el modelo previamente entrenado
model = load_model('deployment_20231111')

# Columnas esperadas por el modelo
cols = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

# 🔧 Nueva función reutilizable para predicción (útil para tests y API)
def predict_charge(dataframe):
    """
    Esta función recibe un DataFrame con los datos del paciente y devuelve
    la predicción del modelo (el costo del seguro).
    """
    prediction = predict_model(model, data=dataframe)
    return prediction['prediction_label'][0]  # ← aquí está el cambio importante

# Página principal
@app.route('/')
def home():
    return render_template("home.html")

# Verificación de salud de la API
@app.route('/health', methods=["GET"])
def health():
    return "HEALTH OK"

# Predicción desde formulario HTML
@app.route('/predict', methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns=cols)
    result = predict_charge(data_unseen)
    return render_template('home.html', pred=f'Expected Bill will be ${int(result)} annually')

# Predicción desde JSON (API)
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    result = predict_charge(data_unseen)
    return jsonify(result)

# Ejecutar la aplicación localmente
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
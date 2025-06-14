import pytest
import numpy as np
import pandas as pd
from app import predict_api  # 👈 Importa la función que debes tener en tu proyecto (ajusta el nombre si es necesario)

# Creamos un conjunto de datos de prueba (un solo registro) con valores válidos
@pytest.fixture
def sample_input():
    """
    Esta función crea un ejemplo de entrada para las pruebas.
    Los datos simulan la información de un paciente.
    """
    return pd.DataFrame([{
        'age': 40,
        'sex': 'male',
        'bmi': 25.0,
        'children': 2,
        'smoker': 'no',
        'region': 'southwest'
    }])

def test_predict_charge_output_type(sample_input):
    """
    Verifica que la función predict_charge devuelva un valor numérico (float o int).
    """
    result = predict_api(sample_input)
    assert isinstance(result, (float, int)), "La predicción debe ser un número."

def test_predict_charge_output_positive(sample_input):
    """
    Verifica que la predicción sea un valor positivo (el costo nunca debe ser negativo).
    """
    result = predict_api(sample_input)
    assert result >= 0, "La predicción debe ser mayor o igual a cero."

def test_predict_charge_output_reasonable_range(sample_input):
    """
    Verifica que la predicción esté dentro de un rango razonable (ejemplo: menos de 100,000).
    Esto evita que un error produzca predicciones absurdas.
    """
    result = predict_api(sample_input)
    assert result < 100000, "La predicción es demasiado alta, verifica el modelo."
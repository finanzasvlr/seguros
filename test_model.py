import pytest
import pandas as pd
from app import predict_charge  # Asegúrate que app.py esté en la misma carpeta o que esté en el PYTHONPATH

@pytest.fixture
def sample_input():
    return pd.DataFrame([{
        'age': 40,
        'sex': 'male',
        'bmi': 25.0,
        'children': 2,
        'smoker': 'no',
        'region': 'southwest'
    }])

def test_predict_charge_output_type(sample_input):
    result = predict_charge(sample_input)
    assert isinstance(result, (float, int)), "La predicción debe ser un número."

def test_predict_charge_output_positive(sample_input):
    result = predict_charge(sample_input)
    assert result >= 0, "La predicción debe ser mayor o igual a cero."

def test_predict_charge_output_reasonable_range(sample_input):
    result = predict_charge(sample_input)
    assert result < 100000, "La predicción parece muy alta."
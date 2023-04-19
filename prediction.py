import joblib
from categorical_values import transform_data

def predict(data, model_name):
    model = joblib.load(f'models/{model_name}')
    transformed_data = transform_data(data)
    return model.predict(transformed_data)
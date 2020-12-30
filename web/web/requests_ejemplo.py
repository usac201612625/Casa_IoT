"""
Cliente HTTP
"""

import requests

URL = 'http://127.0.0.1:8000/proyecto/json_response/'

data = {
    'carnet' : '201700979',
    'nombre' : 'Pedro Alfaro',
    'edad' : 23 ,
}
response = requests.post(URL, data = data)
json_data = response.json()
print(f'Datos enviados por servidor: {json_data}')
print(f'Tipo de datos: {type(json_data)}')
import requests


endpoint = "http://localhost:8000/api/product/133232232327873/"

get_response = requests.get(endpoint)

print(get_response.json())





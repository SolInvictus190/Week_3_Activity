import requests


endpoint = "http://localhost:8000/api/product/1/update/"

data = {"title": " Hello My Old Friend!",
       "price": 140.99
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())





import requests
endpoint="http://127.0.0.1:8000/api/products/143234123/"
get_response=requests.get(endpoint) #Application programming interace
print(get_response.json())

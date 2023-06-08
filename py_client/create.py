import requests
data={'title':'Hey again'}
endpoint="http://127.0.0.1:8000/api/products/"
get_response=requests.post(endpoint,json=data) #Application programming interace
print(get_response.json())

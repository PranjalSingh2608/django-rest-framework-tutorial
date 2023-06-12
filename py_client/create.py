import requests
data={'title':'Hey again'}
headers={'Authorization':'Bearer d035664256986ab8da086ab0e738c62c736eed64'}
endpoint="http://127.0.0.1:8000/api/products/"
get_response=requests.post(endpoint,json=data) #Application programming interace
print(get_response.json())

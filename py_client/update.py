import requests
data={"title":"hello pranjal","price":123.32}
endpoint="http://127.0.0.1:8000/api/products/1/update/"
get_response=requests.put(endpoint,json=data) #Application programming interace
print(get_response.json())

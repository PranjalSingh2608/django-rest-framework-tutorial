import requests
from getpass import getpass
data={'username':'Nat'}
auth_endpoint="http://127.0.0.1:8000/api/auth/"
username=input("what is your username?\n")
password=getpass("What is your password?\n")
auth_response=requests.post(auth_endpoint,json={'username':'Nat','password':password}) #Application programming interace
print(auth_response.json())
if auth_response.status_code==200:
    token=auth_response.json()['token']
    header={
        "Authorization":"Token {token}"
    }
    endpoint="http://127.0.0.1:8000/api/products/"
    get_response=requests.get(endpoint,json=data,headers=header) #Application programming interace
    print(get_response.json())

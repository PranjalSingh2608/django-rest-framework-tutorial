import requests
endpoint="http://127.0.0.1:8000/api/"
get_response=requests.post(endpoint,params={"abc":123},json={"title":"ABC","content":"Hello world"}) #Application programming interace
print(get_response.json())
# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dictionary
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.28.2",
#     "X-Amzn-Trace-Id": "Root=1-647e1d90-19fd3c9f0de2b74558bdc20c"
#   },
#   "json": null,
#   "method": "GET",
#   "origin": "104.28.225.13",
#   "url": "https://httpbin.org/anything"
# }
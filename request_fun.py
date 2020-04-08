import requests

url = str.encode("http://localhost:5000/news")
query = {"query": "tesla"}

s = requests.Session()
x = s.post(url, data=query)
print(x.text)
z = s.get("http://localhost:5000/stock-graph")
print(z)
y = s.get("http://localhost:5000/get-summary")
print(y)

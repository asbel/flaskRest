import requests

BASE = "http://127.0.0.1:5000/"#location of the API/Server it's running on
data = [{"name": "Lilly", "category": "Home", "sunlight":"High"},
{"name": "Bamboo", "category": "Home", "sunlight":"Low"},
{"name": "Palm", "category": "Home", "sunlight":"High"},
{"name": "Cilantro", "category": "Home", "sunlight":"High"}]
for i in range(len(data)):
	response = requests.put(BASE + "plant/"+ str(i),data[i])
	print(response)
input()
#response = requests.delete(BASE + "plant/0")
#print(response)
response = requests.get(BASE + "plant/2")
print(response.json())

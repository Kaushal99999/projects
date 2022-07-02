import requests
url="https://icanhazdadjoke.com/search"

response=requests.get(
	url,
	headers={"Accept":"application/json"},
	params={"term":"cat","limit":1})


data=response.json()
# print(data["joke"])
# print(f"status:{data['status']}")
print(data["results"])
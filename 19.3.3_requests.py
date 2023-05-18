import requests
import json
status = "available"

res_g = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
                     headers={'accept': 'application/json'})

print(res_g.status_code)
print(res_g.text)
print(res_g.json())
print(type(res_g.json()))


url = "https://petstore.swagger.io/v2/pet"
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
data = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)
print(response.status_code)


data["status"] = "available"
data["id"] = "9223372036854760271"
response = requests.put(url, headers=headers, data=json.dumps(data))
print(response.text)
print(response.status_code)


response = requests.delete("https://petstore.swagger.io/v2/pet/9223372036854760271")
print(response.text)
print(response.status_code)

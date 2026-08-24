import requests


url = "https://web-api.tp.entsoe.eu/api?"

params = {
    "documentType": "A65",
    "": "",
    "": "",
}

response = requests.get(
    url,
    params=params
)

print(response.status_code)
print(response.url)
print(response.text)
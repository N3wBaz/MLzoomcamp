import requests
url = 'http://localhost:9696/predict'

client1 = {
    "reports": 0,
    "share": 0.001694,
    "expenditure": 0.12,
    "owner": "yes"
}

client2 = {
    "reports": 0,
    "share": 0.245,
    "expenditure": 3.438,
    "owner": "yes"
}


response = requests.post(url, json=client2).json()
print(response)
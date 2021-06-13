import requests
import json


f = open('./data/pricein.json',)
jsonData = json.load(f)

url = "http://13.233.164.148:8080/api/v1/admin/price-in"

headers = {
  'Content-Type': 'application/json'
}
def pushData(data):
    return requests.request("PUT", url, headers=headers, data=json.dumps(data))

markets=["b94654e3-b04d-4f8c-a6df-466dfca14bb1","e39466a1-f557-4e5f-a9fa-e00868e8dee4","6c75a7eb-3df8-4ec5-acf2-0e50068bee12","46c6a570-a1ac-48cd-8e1f-0945a1e535f3","cdef737f-34b1-43c8-a320-7f2c6556a467"]
for market in markets:
    print(market)
    jsonData['marketId']=market
    print(type(jsonData))
    response=pushData(jsonData)
    print(response.text)

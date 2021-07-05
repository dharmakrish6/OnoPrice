import requests
import json
import random

f = open('./data/pricein.json',)
jsonData = json.load(f)

url = "https://dev-api.onoark.com/v1/daily-price/price/price-in"

headers = {
  'Content-Type': 'application/json'
}
def pushData(data):
    return requests.request("POST", url, headers=headers, data=json.dumps(data))
markets=[
    "cf8abd80-21a2-4297-a5dc-f5527a81ebb5",
    "573afd9e-d8e2-43e5-8c9e-4a24be7c867e",
    "8f5fe511-5415-42b7-9d4f-6f127f3f30f5",
    "a97c172f-c318-4eee-ab70-64ed77f4dabe",
    "e62af834-3c69-4697-9d9a-665497a8cf8a",
    "aaab0c73-8bdd-42ee-bf47-982ac2bbf046",
    "5b61f617-5c03-4135-b50f-efbd507bb1f0",
    "6bc26f1b-93cc-47e0-97e8-914da21d1481",
    "4db36b9f-7fe2-4677-bade-9c2d9c1beb27",
    "ac5d9ecb-df14-452d-b3c9-7f9894934509",
    "4272e37b-c7ae-4a3b-9e1c-5c13f83e7eba",
    "c2c95d2b-bfba-465e-8de6-62d8730ee896",
    "f36bf349-e8a0-4ee3-9898-72eb7b077df7",
    "7872e916-d47a-4e24-8e2c-251bb055eb76",
    "cff66112-b094-4c38-bf2a-c44615d2300e",
    "6aa3cf5a-fd24-44a6-a9ce-c6bfc56f69e0",
    "bef0de12-7971-42d9-bf00-b21b2f7e88aa",
    "c87405b7-ae6f-4e05-8a1a-d9105572e70a",
    "8862134a-7cb6-4da1-ad74-88023f181964",
    "76230152-5f77-4c76-8984-d4cd8658f7b4",
    "5d305134-180a-4bb3-867a-043d840ecd4f",
    "60d67783-da16-4c53-8b36-936ebc5959dc",
    "fa2b086a-2aee-4405-95ca-46643beaf803",
    "f1ce7f8f-f395-4c21-b14f-92e8c3989025",
    "65449b49-460d-47cd-bf22-ddd1403ef909",
    "8e8d0b00-c8a1-49f4-94ea-94292e7cfa9b",
    "b282c4f8-372c-47ba-9b87-92be25551942",
    "53ff78a6-7d81-4171-ad27-4df3ec844e7b",
    "587fa04c-8349-4326-94ce-ab09ab02cceb",
    "b1c9a2b1-02f1-488b-a6e2-971294414b41"
  ]
for market in markets:
    print(market)
    jsonData['marketId']=market
    for each in jsonData['priceIn']:
      each['minPrice']=random.randint(9,20)
      each['maxPrice']=random.randint(21,30)
      each['modalPrice']=(each['minPrice']+each['maxPrice'])/2
    print(type(jsonData))
    response=pushData(jsonData)
    print(response.text)

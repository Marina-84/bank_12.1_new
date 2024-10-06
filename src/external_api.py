import os
from dotenv import load_dotenv
import requests

load_dotenv()
apikey = os.getenv("API_KEY")

def current_conversion(transactions: dict):
    curr_to = "RUB"
    curr_from = transactions["operationAmount"]["currency"]["code"]
    amount = transactions["operationAmount"]["amount"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={curr_to}&from={curr_from}&amount={amount}"
    payload = {}
    headers = {"apikey": "nKc8pYSwLYU0siyO6F8iFw2bnLhAg0Z8"}
    response = requests.get(url, headers=headers, data=payload)
    status_code = response.status_code
    if status_code != 200:
        print(response.reason)
    else:
        result = response.json()
        data = result.get("result")
        print(data)


transactions = {
    "id": 615064591,
    "state": "CANCELED",
    "date": "2018-10-14T08:21:33.419441",
    "operationAmount": {
      "amount": "77751.04",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 3928549031574026",
    "to": "Счет 84163357546688983493"
  }

if __name__ == '__main__':
    current_conversion(transactions)

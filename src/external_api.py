import os
import requests
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("API_KEY")


def current_conversion(transactions: dict):
    curr_to = "RUB"
    curr_from = transactions["operationAmount"]["currency"]["code"]
    amount = transactions["operationAmount"]["amount"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={curr_to}&from={curr_from}&amount={amount}"
    payload: dict = {}
    headers = {"apikey": "nKc8pYSwLYU0siyO6F8iFw2bnLhAg0Z8"}
    response = requests.get(url, headers=headers, data=payload)
    status_code = response.status_code
    if status_code != 200:
        print(response.reason)
    elif curr_from == "RUB":
        return amount
    else:
        result = response.json()
        data = result.get("result")
        return data


transactions = {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  }

if __name__ == "__main__":
    current_conversion(transactions)

from unittest.mock import patch
import pytest
import requests

from src.external_api import current_conversion

transactions = {
    "id": 596171168,
    "state": "EXECUTED",
    "date": "2018-07-11T02:26:18.671407",
    "operationAmount": {
      "amount": "79931.03",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 72082042523231456215"
  }


@patch("requests.get")
def test_current_conversion(mock_get):
    mock_get.return_value.json.return_value = {"result": 79931.03}
    mock_get.return_value.status_code = 200
    assert current_conversion(transactions) == 79931.03

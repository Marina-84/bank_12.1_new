from unittest.mock import patch

import pytest
import requests

from src.external_api import current_conversion

transactions = {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907",
}


@patch("requests.get")
def test_current_conversion(mock_get):
    mock_get.return_value.json.return_value = transactions
    assert current_conversion(transactions) == None

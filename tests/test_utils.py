from unittest.mock import mock_open, patch

from src.utils import get_transactions_list


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_valid_file(mock_file):
    transactions = get_transactions_list("data/operations.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_empty_file(mock_file):
    transactions = get_transactions_list("data/operations.json")
    assert transactions == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file):
    transactions = get_transactions_list("data/operations.json")
    assert transactions == []

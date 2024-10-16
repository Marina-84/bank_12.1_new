from typing import Any
import re
from collections import Counter


def sort_by_date(list_dictionaries: list[dict[str, Any]], reverse: Any = True) -> list[dict[str, Any]] | bool:
    """Функция фильтрует словари по дате"""
    sorted_dict = sorted(list_dictionaries, key=lambda x: x["date"], reverse=reverse)
    return sorted_dict


def filter_by_state(list_dictionaries: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]] | str:
    """Функция возвращает словари с указанным параметром"""
    state_dictionary = []
    for key in list_dictionaries:
        if key.get("state") == state_id:
            state_dictionary.append(key)
    return state_dictionary


def filter_by_request(transaction_list: list[dict], user_request: str) -> list[dict]:
    """Function filter transactions by user request."""

    target_list = []
    lower_user_request = user_request.lower()
    for transaction in transaction_list:
        if re.search(lower_user_request, transaction.get("description", ""), flags=re.IGNORECASE):
            target_list.append(transaction)
        else:
            continue
    print(target_list)
    return target_list


def count_transaction_categories(transactions: list[dict]) -> dict:
    """ Функция считает количество транзакций, сортируя их по категориям """

    categories = []
    for transaction in transactions:
        categories.append(transaction["description"])
    counted = dict(Counter(categories))
    print(counted)
    return counted

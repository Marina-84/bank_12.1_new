from typing import Any


def sort_by_date(list_dictionaries: list[dict[str, Any]], reverse=True) -> list[dict[str, Any]] | bool:
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

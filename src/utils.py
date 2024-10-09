import json


def get_transactions_list(path: str) -> list[dict]:
    """Возвращает список словарей с данными о финансовых транзакциях"""
    error_list: list[dict] = []
    try:
        with open(path, encoding="utf-8") as f:
            try:
                transactions_list = json.load(f)
            except json.JSONDecodeError:
                print("Введены некорректные данные")
                return error_list
    except FileNotFoundError:
        print("Файл не найден")
        return error_list

    return transactions_list


if __name__ == "__main__":
    get_transactions_list("C:\\Users\\marin\\PycharmProjects\\my_prj\\bank_10.2_new\\data\\operations.json")

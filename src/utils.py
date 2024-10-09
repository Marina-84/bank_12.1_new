import json
import logging
import os

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_log_file_path = os.path.join(current_dir, "../log/utils.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)

# Создаем путь до файла JSON относительно текущей директории
rel_src_file_path = os.path.join(current_dir, "../data/operations.json")
abs_src_file_path = os.path.abspath(rel_src_file_path)

# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_list(path: str) -> list[dict]:
    """Возвращает список словарей с данными о финансовых транзакциях"""
    error_list: list[dict] = []
    try:
        with open(path, encoding="utf-8") as f:
            try:
                logger.info("Путь до файла json верный")
                transactions_list = json.load(f)
            except json.JSONDecodeError:
                logger.warning("Введены некорректные данные")
                return error_list
    except FileNotFoundError:
        logger.warning("Файл не найден")
        return error_list

    return transactions_list


if __name__ == "__main__":
    get_transactions_list("C:\\Users\\marin\\PycharmProjects\\my_prj\\bank_10.2_new\\data\\operations.json")

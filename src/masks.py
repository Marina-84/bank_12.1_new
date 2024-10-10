import logging
import os

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_file_path = os.path.join(current_dir, "../log/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_num: str) -> str:
    """Функция возвращает маску номера карты"""
    if len(card_num) == 16:
        logger.info("Формат карты верный")
        return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[12:]}"
    else:
        logger.warning("Неверный формат банковской карты")
        return "Неверный формат банковской карты"


def get_mask_account(acc_num: str) -> str:
    """Функция возвращает маску номера счета"""
    if len(acc_num) == 20:
        logger.info("Формат счета верный")
        return f"**{acc_num[-4:]}"
    else:
        logger.warning("Неверный формат счета")
        return "Неверный формат номера счета"


if __name__ == "__main__":
    get_mask_card_number("3888884567895678")

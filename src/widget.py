from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data_card: str) -> str:
    """Функция обрабатывает информацию о картах и счетах"""
    card_name = ""
    card_number = ""
    for s in data_card:
        if s.isdigit():
            card_number += s
        else:
            card_name += s
    if len(card_number) == 16:
        number_mask = get_mask_card_number(card_number)
        card_mask = card_name + number_mask
        return card_mask
    else:
        number_mask = get_mask_account(card_number)
        card_mask = card_name + number_mask
        return card_mask


def get_date(incoming_date: str) -> str:
    """Функция возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    slice_date = incoming_date[:10]
    date_new = ""
    for one_symbol in range(len(slice_date)):
        if slice_date[one_symbol].isdigit():
            date_new += slice_date[one_symbol]
        else:
            date_new += " "
    date_new_split = date_new.split()
    split_date = date_new_split[::-1]
    final_result = ".".join(split_date)
    return final_result

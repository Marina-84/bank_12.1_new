def get_mask_card_number(card_num: str) -> str:
    """Функция возвращает маску номера карты"""
    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[12:]}"


def get_mask_account(acc_num: str) -> str:
    """Функция возвращает маску номера счета"""
    return f"**{acc_num[-4:]}"

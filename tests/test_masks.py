import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_num, mask",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
    ],
)
def test_mask_card_number(card_num: str, mask: str) -> None:
    """Тестирование функции на обработку входных данных"""
    assert get_mask_card_number(card_num) == mask


def test_mask_account() -> None:
    """Тестирование функции на обработку входных данных"""
    assert get_mask_account("64681647367889477958") == "**7958"

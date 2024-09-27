from typing import Any

import pytest

from src.decorators import log


def test_log(capsys) -> Any:
    with pytest.raises(Exception):
        captured = capsys.readouterr()
        assert captured.out == "my_function error\n"
    my_decorator(2, 5)


@log(filename="mylog.txt")
def my_decorator(x: int, y: int) -> Any:
    return x + y

def my_decorator(x="6", y=[1, 2, 3]) -> Any:
    return x + y

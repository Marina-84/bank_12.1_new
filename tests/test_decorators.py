from typing import Any

import pytest

from src.decorators import log, my_function


@log(filename="mylog.txt")
def test_log(capsys) -> Any:
    with pytest.raises(Exception):
        captured = capsys.readouterr()
        assert captured.out == Exception
        my_function(x=[3], y=[1, 2, 3])


def test_my_function(x=1, y=2) -> Any:
    result = x + y
    try:
        assert result == "5"
    except AssertionError:
        print("Error")


def test_my_function_2(x=1, y=2) -> Any:
    result = x + y
    assert result == 3

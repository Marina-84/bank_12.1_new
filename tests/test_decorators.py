from typing import Any
from src.decorators import log
import pytest


def test_correct_log_in_console(capsys):
    @log()
    def my_function(x: Any, y: Any) -> Any:
        """Функция складывает два значения"""
        return x + y

    my_function(1, 2)
    print('my_function ok')
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_correct_log_in_file():
    @log(filename='test.log')
    def my_function(x: Any, y: Any) -> Any:
        """Функция складывает два значения"""
        return x + y

    my_function(1, 2)
    with open("test.log") as f:
        row = f.read().split("\n")[0]
    assert row == "my_function ok"


def test_incorrect_log_in_console(capsys):
    @log()
    def my_function(x: Any, y: int) -> Any:
        """Функция складывает два значения"""
        return x + y

    my_function(1, '2')
    print('my_function error')
    captured = capsys.readouterr()
    assert captured.out == "my_function error\n"


def test_incorrect_log_in_file():
    @log(filename='test.log')
    def my_function(x: int, y: int) -> int:
        try:
            with pytest.raises(TypeError, match='my_function error'):
                my_function('1', '2')
        finally:
            with open("test.log") as f:
                row = f.read().split("\n")[0]
                assert row == "my_function error"


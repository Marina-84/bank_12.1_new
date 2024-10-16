from typing import Any

from src.decorators import log


def test_correct_log_in_console(capsys) -> Any:
    @log()
    def my_function(x: Any, y: Any) -> Any:
        """Функция складывает два значения"""
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_correct_log_in_file() -> Any:
    @log(filename="test.log")
    def my_function(x: Any, y: Any) -> Any:
        """Функция складывает два значения"""
        return x + y

    my_function(1, 2)
    with open("test.log") as f:
        row = f.read().split("\n")[0]
    assert row == "my_function ok"


def test_incorrect_log_in_console(capsys) -> Any:
    @log()
    def my_function(x: Any, y: Any) -> Any:
        """Функция складывает два значения"""
        return x + y

    my_function(1, "2")
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError. Inputs: (1, '2'), {}\n"


def test_incorrect_log_in_file() -> Any:
    @log(filename="test.log")
    def my_function(x: Any, y: Any) -> Any:
        """Функция складывает два значения"""
        return x + y

    my_function(1, "2")
    with open("test.log") as f:
        row = f.read().split("\n")[0]
    assert row == "my_function error: TypeError. Inputs: (1, '2'), {}"

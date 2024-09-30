from typing import Any, Callable, Optional


def log(filename: Optional[str] = "test.log") -> Callable:
    """Декоратор создает логирование в функции."""

    def my_decorator(func) -> Any:
        def wrapper(*args: int, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
        return wrapper
    return my_decorator


@log(filename="test.log")
def my_function(x: Any, y: Any) -> Any:
    """Функция складывает два значения"""
    return x + y


my_function(1, 2)

from functools import wraps
from typing import Callable, Optional, Any


def log(filename: Optional[str]) -> Callable:
    """Декоратор создает log в функции."""

    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                # time_1 = time()
                result = func(*args, **kwargs)
                # time_2 = time()
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                raise e

        return wrapper

    return my_decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """Функция складывает два значения"""
    return x + y


my_function(2, 5)

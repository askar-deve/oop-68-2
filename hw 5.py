import time
from functools import total_ordering


def timer (func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} работала {execution_time} сек.")
        return result
    return wrapper
@timer
def something(arg):
    total = 0
    for i in range(arg):
        total += i
    return arg


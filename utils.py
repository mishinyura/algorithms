import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время работы {func.__name__}: {end - start:.6f} секунд')
        return result
    return wrapper

import time


def how_long(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f'Программа выполнена за {end_time - start_time}')
        return res

    return wrapper






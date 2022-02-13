import time


def how_long(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f'Программа выполнена за {end_time - start_time}')
        return res

    return wrapper


@how_long
def main_def(a):
    res = 0
    for i in range(a + 1):
        res += i

    return res


@how_long
def some_def(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i ** 2)

    return new_lst


result = main_def(10000 * 10000)
print(result)
result_2 = some_def([i for i in range(15)])
print(result_2)



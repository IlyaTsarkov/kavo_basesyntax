my_lst = [1, 4, 'hello', 5.5, [100, 200], '50']


def lst_sum():
    res = 0
    for i in my_lst:
        if isinstance(i, int):
            res += i

    return res


result = lst_sum()
print(result)



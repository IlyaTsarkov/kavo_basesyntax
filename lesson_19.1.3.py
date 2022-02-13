a, b, *c = [1, 2, 3, 4, 5]
print(a, b, c)
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)
*a, b, c = [1, 2, 3, 4, 5]
print(a, b, c)
*a, b, c = [1, 2]
print(a, b, c)


def amount(**kwargs):
    ex_dict = {}
    for key, value in kwargs.items():
        ex_dict[key] = value

    return ex_dict


res = amount(a=1, b=2, c=3, d=4, e=5)
print(res)
res_2 = amount(a=5, b=2, c=3)
print(res_2)

def some_def(a, b, c):
    return a * b * c


res = some_def(5, 10, 15)
print(res)

result = lambda a, b, c: a * b * c

print(result(5, 10, 15), '\n')


def some_def_2(x):
    return x ** x


res_2 = some_def_2(5)
print(res_2)

result_2 = lambda x: x ** x

print(result_2(5))



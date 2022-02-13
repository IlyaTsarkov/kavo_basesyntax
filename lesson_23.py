def gen_func(lst):
    for x in lst:
        yield x


res = gen_func([1, 2, 3, 4, 5, 6])
print(res)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))



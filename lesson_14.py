ex_set = {1, 'two', 3, 4, False}
print(ex_set)
print(type(ex_set))

lst = [1, 3, 2, 2, 3, 1, 5, 6]
print(set(lst))

ex_str = 'abrakadabra'
print(set(ex_str))

ex_set.add(10)
print(ex_set)
ex_set.update(range(5, 7))
print(ex_set)
ex_set.discard(6)
print(ex_set)
ex_set.remove('two')
print(ex_set)



list_a = [[x for x in range(1, 5)] for y in range(1, 4)]
print(list_a)

list_b = [[x ** 2 for x in lst_a] for lst_a in list_a]
print(list_b)



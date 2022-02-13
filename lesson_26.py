lst_1 = [x for x in range(7)]
lst_2 = [x for x in range(4)]
lst_3 = 'abcdefgh'

res = zip(lst_1, lst_2, lst_3)
for i, i1, i2 in res:
    print(i, i1, i2)



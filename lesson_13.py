dct_1 = {1: 'one', 2: 'two', 3: 'three'}

for key, value in dct_1.items():
    print(key, value)

dct_2 = {4: 'four', 5: 'five', 6: 'six'}

dict_3 = {**dct_1, **dct_2}
print(dict_3)



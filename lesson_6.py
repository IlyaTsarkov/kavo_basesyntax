list_11 = [1, 2, 3, [1, 2, ['hello', 'abc'], 3], 4, [2, 'cba']]
print(len(list_11))
print(list_11[3])
print(list_11[3][2])
print(list_11[3][2][1])

list_1_1 = [1, 10, -12]
list_2_2 = ['b', 'c', 'wd']
list_3_3 = list_1_1 + list_2_2
list_4_4 = list_3_3 * 2
print(list_3_3)
print(list_4_4)
print(list_1_1 + [1, 2, 3])

list_1 = [1, 10, -12, 4.89, 5, 11.2]
list_2 = ['b', 'c', 'wd', 'g', 'a', 'e']
print(sorted(list_1))
print(sorted(list_2))
print(list_1)
print(list_2)
print(sorted(list_1, reverse=True))

list_4 = ['hello', 'ivan', 'ivanov']
list_3 = ['hello', 3.4, 'abc']
string = 'hello'
print(list(string))
print(list_1[2])
print(list_2[1])
print(list_3[0:2])



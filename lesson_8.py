a = int(input('Введите число '))

res = (print('<10') if a < 10 else print('>10')) if a % 2 == 0 else print('нечетное')

b = int(input('Введите 3 '))

ex_list = [1, 2, b if b == 3 else print('Я же просил'), 4, 5]
print(ex_list)



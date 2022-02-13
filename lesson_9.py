n = 0
even_list = []
not_even_list = []

while n < 5:
    a = int(input('Введите цифру: '))
    if a % 2 == 0:
        even_list.append(a)
    else:
        not_even_list.append(a)
    n += 1
    if n == 4:
        break
    elif n == 2:
        continue

    print('Отработал')

else:
    print('n больше четырех')

mes = input('Напишите Четное/Нечетное ')
if mes.lower() == 'четное':
    print(even_list)
elif mes.lower() == 'нечетное':
    print(not_even_list)
else:
    print('Неизвестная команда')



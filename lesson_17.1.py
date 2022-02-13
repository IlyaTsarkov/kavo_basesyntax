even_list = [x for x in range(11) if x % 2 == 0]
print(even_list)

sec_list = [x for x in range(17) if x % 2 != 0 and x > 5]
print(sec_list)

new_list = even_list + sec_list
print(new_list)

ev_or_not = ['even' if x % 2 == 0 else 'not_even' for x in new_list]
print(ev_or_not)


n = 5

ex_list = []
for x in range(n):
    ex_list.append(x ** 2)

print(ex_list)

ex_comp_list = [x ** 2 for x in range(n)]
print(ex_comp_list)



from lesson_29for_import import how_long


@how_long
def main(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i ** 2)

    return sum(new_lst)


res = main([x for x in range(1000 * 10000)])
print(res)

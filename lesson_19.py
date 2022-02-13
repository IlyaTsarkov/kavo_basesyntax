a = 100


def some_def():
    a = 200

    def some_def_2():
        nonlocal a
        a = 50
        print(a)

    some_def_2()
    print(a)


some_def()
print(a)



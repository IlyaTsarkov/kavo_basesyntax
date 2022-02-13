def rec_def(n):
    if n <= 3:
        print('До')
        rec_def(n + 1)
        print('После')


rec_def(1)



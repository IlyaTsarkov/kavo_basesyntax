my_str = map(str, input().split())
res = filter(lambda x: len(x) < 5, my_str)
for i in res:
    print(i)
    
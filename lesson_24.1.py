x = list(map(int, input().split()))

res = map(abs, x)
for i in res:
    print(i, end=' ')



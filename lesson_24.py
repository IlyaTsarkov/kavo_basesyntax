lst = [x for x in range(6)]
res = map(str, lst)
print(next(res))

for i in res:
    print(i)
    print(type(i))
    

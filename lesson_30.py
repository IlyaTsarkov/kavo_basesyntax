with open(file="files/new.txt", encoding="utf-8", mode='a') as ex:
    ex.write('Строка 4')


with open(file="files/new.txt", encoding="utf-8", mode='a+') as ex:
    ex.write('Строка 5')
    ex.seek(0)
    print(ex.read())



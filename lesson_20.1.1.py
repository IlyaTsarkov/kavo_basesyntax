def your_name(name):
    def say_hello():
        print(f'Hello {name}')

    return say_hello


ex = your_name('Ilya')
second_ex = your_name('Jora')
ex()
second_ex()




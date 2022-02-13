def your_name(name):
    def say_hello():
        print(f'Hello {name}')

    say_hello()


your_name('Ilya')

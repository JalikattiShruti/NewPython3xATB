def my_decorator(func):
    def wrapper():
        print("Started")
        print("/////////")
        func()
        print
        print("/////////")
        print("Completed")

    return wrapper()

@my_decorator
def say_hello():
    print("say_hello")
say_hello()


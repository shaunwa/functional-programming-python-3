def create_spy(func_name):
    def inner(func):
        def spy_func(arg):
            print(f"The {func_name} function was called!")
            return func(arg)
        return spy_func
    return inner

@create_spy('double')
def double(x):
    return x * 2

@create_spy('square')
def square(x):
    return x * x

@create_spy('greet')
def greet(name):
    print(f"Hello, {name}")

answer = double(square(10))
greet('Shaun')
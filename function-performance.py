import datetime

def create_spy(func_name):
    def inner(func):
        def spy_func(arg):
            print(f"The {func_name} function was called!")
            return func(arg)
        return spy_func
    return inner

def add_performance_watch(func):
    def inner(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        total_time = end - start
        print(f'The {func.__name__} function executed in {total_time}')
        return result
    
    return inner

@create_spy('double')
@add_performance_watch
def double(x):
    return x * 2

@create_spy('square')
@add_performance_watch
def square(x):
    return x * x

@create_spy('greet')
@add_performance_watch
def greet(name):
    print(f"Hello, {name}")

answer = double(square(12))
greet("Shaun")
import datetime

def print_stats(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        total_time = end - start

        stats = {
            'args': args,
            'kwargs': kwargs,
            'result': result,
            'total_time': total_time
        }

        print(stats)

        return result
    
    return wrapper

@print_stats
def double(x):
    return x * 2

@print_stats
def square(x):
    return x * x

@print_stats
def add(x, y, z):
    return x + y + z

@print_stats
def greet(name):
    print(f"Hello, {name}")

square(10)
add(5, 6, z=10)
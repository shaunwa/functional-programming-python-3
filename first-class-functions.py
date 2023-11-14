def add_numbers(x, y):
    return x + y

print(add_numbers(10, 14))

x = 4
message = "Hello"
my_function = add_numbers

print(my_function(10, 14))

# Example

def load_data_real():
    print('Loading data from a third-party api...')
    return [100, 200, 300]

def load_data_fake():
    return [1, 2, 3]

mode = 'DEV'

load_data = load_data_real if mode == 'PROD' else load_data_fake

data = load_data()

print(data)

# Passing functions as arguments

def subtract_numbers(x, y):
    return x - y

def combine_10_and_11(func):
    return func(10, 11)

print(combine_10_and_11(subtract_numbers))

# Returning functions

def create_printer(name):
    def say_hello():
        print(f"Hello from inside another function, {name}!")

    return say_hello

printer_1 = create_printer("Shaun")
printer_1()

printer_2 = create_printer("Bob")
printer_2()

printer_3 = create_printer("Sue")
printer_3()
# 1. Immutability

x = 5

# ...

x = 100 # This is NOT allowed in functional programming

# 2. First-class Functions

y = 4
message = "Hello"
is_working = False

def my_function_1():
    return "Hello"

def my_function_2():
    print("Hi")

def my_function_3():
    print("Hello")

my_numbers = [1, 2, 3, 4, 5]
my_functions = [my_function_1, my_function_2, my_function_3]

# 3. Pure Functions (Separation of Functions and Data)

external_var = 42

# This is not a pure function
def my_function():
    print(f"The value of external_var is {external_var}")

# This is a pure function
def add_numbers(a, b, c):
    return a + b + c

print(add_numbers(1, 2, 3))
print(add_numbers(1, 2, 3))
print(add_numbers(1, 2, 3))

class Person:
    def __init__(self):
        self.name = "Shaun"

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

person_1 = Person()
print(person_1.get_name())
person_1.set_name("John")
print(person_1.get_name())
person_1.set_name("Bob")
print(person_1.get_name())
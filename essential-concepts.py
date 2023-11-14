# Imperative vs. Declarative

numbers = [1, 2, 68, 27, 100, -4]

def calculate_and_print_average(numbers):
    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)

    print(f'The average is: {average}')

# The declarative way:

def average(numbers):
    return sum(numbers) / len(numbers)

# print(f'The average is: {sum(numbers) / len(numbers)}')

# 1. Immutability

x = 5

pi = 3.14159

# data = load_data_from_db()

# updated_data = map(lambda user: { **user, "name": "ABC" }, data)

# write_data_to_db(updated_data)

# 2. Pure Functions

external_var = 42

def my_function():
    return 1 + external_var

def do_something():
    # Writes data to the database
    return 100

print(my_function())
print(my_function())

external_var = 1000

print(my_function())
print(my_function())

def add(x, y):
    return x + y

print(add(10, 11))
print(add(10, 11))
print(add(10, 11))
print(add(10, 11))

import random

def random_digit():
    return random.randint(0, 9)

print(random_digit())
print(random_digit())
print(random_digit())
print(random_digit())

# 3. Simple Data Structures

person = { "name": "Shaun", "age": 123, "hair_color": "brown" }
dog = { "name": "Paws", "breed": "Golden Retriever" }

updated_person = { **person, "name": "John" }

def get_name(dictionary):
    return dictionary["name"]

def uppercase(string):
    return string.upper()

print(uppercase(get_name(person)))
print(uppercase(get_name(dog)))

# 4. First-Class Functions
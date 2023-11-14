numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled = []

for number in numbers:
    doubled.append(number * 2)

def double(x):
    return x * 2

def add_5(x):
    return x + 5

doubled_numbers = list(map(double, numbers))
numbers_plus_5 = list(map(add_5, numbers))

print(doubled_numbers)
print(numbers_plus_5)

doubled_numbers2 = [x * 2 for x in numbers]
numbers_plus_5_2 = [x + 5 for x in numbers]

print(doubled_numbers2)
print(numbers_plus_5_2)

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

def is_even(x):
    return x % 2 == 0

evens = list(filter(is_even, numbers))

evens_2 = [x * 5 for x in numbers if x % 2 == 0]
big_numbers = [x for x in numbers if x > 5]

print(evens)

is_any_even = any(map(is_even, numbers))
is_all_even = all(map(is_even, evens))

print(is_any_even)
print(is_all_even)


numbers_1 = [1, 2, 3]
numbers_2 = [4, 5, 6]

combined_numbers = [*numbers_1, *numbers_2]

print(combined_numbers)

person = { "name": "Shaun", "age": 123, "hair_color": "brown" }

updated_person = { **person, "hair_color": "grey" }

def print_args(*args, **kwargs):
    print(f'The args are: {kwargs}')

numbers = [1, 2, 3, 4]

print_args(*numbers, **person)

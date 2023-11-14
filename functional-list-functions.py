# Map

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5, 101]

doubled_numbers = list(map(double, numbers)) # Doubling all of the numbers

print(doubled_numbers)

def subtract_one(x):
    return x - 1

numbers_minus_one = list(map(subtract_one, numbers)) # Subtracting one from all of the numbers

print(numbers_minus_one)

# Filter

# big_numbers = []

# for x in numbers:
#     if x > 3:
#         big_numbers.append(x)

def is_greater_than_3(x):
    return x > 3

big_numbers = list(filter(is_greater_than_3, numbers))

print(big_numbers)

# Any

def is_greater_than_100(x):
    return x > 100

if any(map(is_greater_than_100, numbers)):
    print("There is a number greater than 100")
else:
    print("None of the numbers are greater than 100")

# All

if (all(map(is_greater_than_100, [1, 105, 200, 755]))):
    print("All of the numbers are greater than 100")
else:
    print("Not all of the numbers are greater than 100")

# List Comprehensions

doubled_numbers = [x * 2 for x in numbers]
print(doubled_numbers)

big_numbers = [x for x in numbers if x > 3]
print(big_numbers)
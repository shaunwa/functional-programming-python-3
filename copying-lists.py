from copy import *

numbers = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]

combined_numbers = copy(numbers)

for number in numbers_2:
    combined_numbers.append(number)

print(combined_numbers)
print(numbers)
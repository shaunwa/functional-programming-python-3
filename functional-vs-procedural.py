numbers = [54, 3, 6, 10, 37, 100, -5]

def get_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total

total = get_total(numbers)

print(total)
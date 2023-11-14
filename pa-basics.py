def add(x, y, z):
    return x + y + z

def curried_add(x):
    def inner(y):
        def inner_inner(z):
            return add(x, y, z)

        return inner_inner

    return inner

add1 = curried_add(1)

add_1_and_2 = add1(2)

print(add_1_and_2(3))
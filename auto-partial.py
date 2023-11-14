from inspect import signature

def partially_apply(func):
    def auto_partial_wrapper(*accumulated_args):
        num_of_args = len(signature(func).parameters)

        if len(accumulated_args) >= num_of_args:
            return func(*accumulated_args)

        def inner(*new_args):
            new_acc_args = [*accumulated_args, *new_args]

            if len(new_acc_args) >= num_of_args:
                return func(*new_acc_args)
            else:
                return auto_partial_wrapper(new_acc_args)

        return inner
    
    return auto_partial_wrapper

@partially_apply
def add(x, y, z):
    return x + y + z

add1 = add(1)
print(add1(10, 20))

add_2_and_3 = add(2, 3)
print(add_2_and_3(3))

print(add(1, 2, 3))
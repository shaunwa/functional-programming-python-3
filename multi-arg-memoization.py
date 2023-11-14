def memoize(func):
    results = {}

    def memoized(*args):
        arg_str = str(args)

        if arg_str in results:
            print('Found previously cached result!')
            return results[arg_str]
        else:
            print('Calculating new result...')
            new_result = func(*args)
            results[arg_str] = new_result
            return new_result

    return memoized

@memoize
def add(x, y, z):
    return x + y + z

print(add(1, 2, 3))
print(add(1, 2, 3))
print(add(2, 4, 6))
print(add(2, 4, 6))
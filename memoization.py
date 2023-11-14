# 0 1 2 3 4 5 6  7  8  ...
# 1 1 2 3 5 8 13 21 34 

cached_results = {}

def fib(x):
    if x in cached_results:
        return cached_results[x]
    else:
        new_result = 1 if x <= 1 else fib(x - 1) + fib(x - 2)
        cached_results[x] = new_result
        print(cached_results)
        return new_result

print(fib(50))
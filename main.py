def test(*args):
    for i in range(len(args)):
        print(args[i])

def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    else:
        return n

test(1, 2, 3, 'рис', 'нори', 'угрь', True, False)

print(factorial(6))
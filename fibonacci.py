def fib_loop_while(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a + b
        max -= 1
        yield a


for i in fib_loop_while(10):
    print(i)


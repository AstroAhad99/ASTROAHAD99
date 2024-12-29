def counter(n):
    while n > 0:
        yield(n)
        n -= 1

c1 = counter(10)
c2 = counter(20)
print(next(c1))
print(next(c2))
print(next(c1))
print(next(c2))
# This program prints out the which numbers are prime in the certain range
# This program also shows that (else) operation can also be performed with the FOR loop
# when for n in range(2, 2). this line will not run which is the forst iteration. Very important


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number.")

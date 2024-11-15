# Creating a fabbonaci series by updating the variables
# 0, 1, 1, 2, 3, 5, 8, 13, .........

a = 0
print(a)
b = 1
print(b)
for i in range(20):
    c = a + b
    a = b
    b = c
    print(c)
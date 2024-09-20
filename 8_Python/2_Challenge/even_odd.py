# # This program is used to check if the number is even or odd

# num = 3

# if num % 2 == 0:
#     print("This number", str(num), "is even.")
# else:
#     print("This number", str(num), "is odd.")

# This program checks if the both numbers that are input are even, odd, or either 1 of them is even

num_a = 2
num_b = 4

sum_a_b = num_a + num_b

print(sum_a_b)

if sum_a_b % 2 == 0:
    if num_a % 2 == 0:
        print("Both numbers are even.")
    else:
        print("Both numbers are odd.")
else:
    print("Only 1 number is even.")
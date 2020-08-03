# Write a program to find the sum of all the odd numbers for a given limit

limit = int(input("Enter a limit"))
oddSum = 0
i = 0

for i in range(limit):
    if i % 2 != 0:
        oddSum = oddSum + i

print("Sum of odd numbers:", oddSum)

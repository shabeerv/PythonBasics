# Write a program to print the following pattern using for loop

m = 1
n = 6

for i in range(1, n):
    for j in range(1, i):
        print(m, end=' ')
        m += 1
    print()

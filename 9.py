# Write a program to print the following pattern (hint: use nested loop)

m = 5

for i in range(1, m+1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")

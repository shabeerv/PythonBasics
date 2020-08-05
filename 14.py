# Write a program to add to two dimensional arrays

array = []
array1 = []
result = []

size = int(input("Enter the size of arrays:"))

for i in range(size):
    values = []
    for j in range(size):
        values.append(0)
    result.append(values)

print("Enter the values of array 1")
for i in range(size):
    values = []
    for j in range(size):
        values.append(int(input()))
    array.append(values)

print("Enter the values of array 2")
for i in range(size):
    values = []
    for j in range(size):
        values.append(int(input()))
    array1.append(values)

for i in range(size):
    for j in range(size):
        result[i][j] = array[i][j] + array1[i][j]

print("Sum of 2 arrays is:")

for i in result:
    print(i)

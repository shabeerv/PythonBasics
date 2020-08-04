# Write a program to interchange the values of two arrays.

array = []
array1 = []

size = int(input("Enter the size of arrays:\n"))

print("Enter the values of Array 1:\n")
for i in range(0, size):
    values = int(input())

    array.append(values)

print("Enter the values of Array 2:\n")
for i in range(0, size):
    values = int(input())

    array1.append(values)

for i in range(0, size):
    temp = array[i]
    array[i] = array1[i]
    array1[i] = temp

print("Arrays after swapping:")
print("Array 1:")
for i in range(0, size):
    print(array[i], end=', ')

print("\nArray 2:")
for i in range(0, size):
    print(array1[i], end=', ')

# Write a program to sort an array in descending order

array = []
size = int(input("Enter the size of array:\n"))

print("Enter the values of array")
for i in range(0, size):
    values = int(input())
    array.append(values)

for i in range(0, size):
    for j in range(i+1, size):
        if array[i] < array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

print("Sorted array:")
for i in range(0, size):
    print(array[i], end=',')

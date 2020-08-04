# Write a program to find the number of even numbers in an array

array = []
count = 0
size = int(input("Enter the size of an array:\n"))

print("Enter the values of array:\n")
for i in range(0, size):
    values = int(input())
    array.append(values)

    if array[i] % 2 == 0:
        count += 1
print("Number of even numbers in the given array is", count)

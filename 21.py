# Write a program to multiply the adjacent values of an array and store it in an another array

array = []
result = []
limit = int(input("Enter the array limit: "))

for i in range(limit):
    result.append(0)

for i in range(limit):
    values = int(input())
    array.append(values)

for i in range(limit):
    k = i + 1
    if k < limit:
        result[i] = array[i]*array[i + 1]
        print(result[i], end=' ')

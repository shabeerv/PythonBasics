# Write a program to add the values of two 2D arrays

array = []
array1 = []
result = []


def get_array(size):
    for i in range(size):
        values = []
        for j in range(size):
            values.append(0)
        result.append(values)
    print("Enter the values of array 1 ")
    for i in range(size):
        values = []
        for j in range(size):
            values.append(int(input()))
        array.append(values)

    print("Enter the values of array 2 ")
    for i in range(size):
        values = []
        for j in range(size):
            values.append(int(input()))
        array1.append(values)


def add_array(size):
    for i in range(size):
        for j in range(size):
            result[i][j] = array[i][j] + array1[i][j]


def display_array():
    print("Sum of array 1 and array 2: ")
    for i in result:
        print(i)


def main():
    size = int(input("Enter the size of arrays: "))
    get_array(size)
    add_array(size)
    display_array()


main()

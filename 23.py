# Write an object oriented program in java to store and display the values of a 2D array

size = int(input("Enter the size of array"))
array = []


def get_array():
    print("Enter the array values")

    for i in range(size):
        values = []
        for j in range(size):
            values.append(int(input()))
        array.append(values)


def display_array():
    for i in array:
        print(i)


get_array()
display_array()

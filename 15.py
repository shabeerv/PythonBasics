# Write a program to accept an array and display it on the console using functions

array = []


def get_array(size):
    for i in range(size):
        values = int(input())
        array.append(values)


def display_array():
    print(array, end=' ')


def main():
    size = int(input("Enter the size of array:"))
    get_array(size)
    display_array()


main()

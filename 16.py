# Write a program to check whether a given number is prime or not

num = int(input("Enter a number:"))
flag = 0

for i in range(2, num):
    if i <= num / 2:
        if num % 2 == 0:
            flag = 1
            break
if flag == 0:
    print("Entered number is a Prime number")
else:
    print("Entered number is not a Prime number")

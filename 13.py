# Write a program to identify whether a string is a palindrome or not

string = input("Enter a string:\n")
length = ""
isPalindrome = 0

for i in string:
    length = i + length
    if string == length:
        isPalindrome = 1
        break

if isPalindrome == 1:
    print("Entered string is palindrome")
else:
    print("Entered string is not palindrome")

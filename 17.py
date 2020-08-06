# Write a menu driven java program to do the basic mathematical operations such as addition, sub, multiplication and div

class SimpleCalculator:

    def __init__(self):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        total = self.num1 + self.num2
        return total

    def subtraction(self):
        sub = self.num1 - self.num2
        return sub

    def multiplication(self):
        mul = self.num1 * self.num2
        return mul

    def division(self):
        div = self.num1 / self.num2
        return div


num1 = int(input("Enter two numbers: "))
num2 = int(input())

calc = SimpleCalculator()

choice = 1
while choice != 5:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Result:", calc.addition())
    elif choice == 2:
        print("Result:", calc.subtraction())
    elif choice == 3:
        print("Result:", calc.multiplication())
    elif choice == 4:
        print("Result:", calc.division())
    elif choice == 5:
        print("Exiting!")
    else:
        print("Invalid choice")

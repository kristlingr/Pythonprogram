'''Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
'''
usr_num = int(input("Enter a number: "))
def factorial(num):
    if num < 2:
        return 1
    else:
        return num*factorial(num-1)

result = factorial(usr_num)
print(f"The factorial of {usr_num} is {result}")

'''Task-2 Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
'''
import math

user_num1 = int(input("Enter a number: ")) #asking user to give number

if user_num1 > 0:
    print("Square root:", math.sqrt(user_num1))
    print("logarithm :", math.log(user_num1))
    print("Sine :", math.sin(user_num1))
else:
    print("check the input")





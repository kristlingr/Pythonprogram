'''Task -1 Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.'''

number1 = input("Enter first numbers: ")
number2 = input("Enter second numbers: ")

number1 = int(number1)
number2 = int(number2)
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2

print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)


''' Task -2 Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
'''
firstname= input("enter your first name:")
lastname= input("enter your last name:")
fullname= firstname+ " " + lastname

print(f"Hello, {fullname}!, Welcome to Python  learning program.")
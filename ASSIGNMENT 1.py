'''Task -1 Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.'''

user_input = int(input("Enter first numbers: "))
user_input1 = int(input("Enter second numbers: "))

# Mathematical operation A. addition

addition = user_input + user_input1
print(f"Addition: {addition}")
# b.subtraction
subtraction = user_input - user_input1
print(f"Subtraction: {subtraction}")
# c.,multipication

mul= user_input*user_input1
print(f"Multiplication: {mul}")
# d.division

divi= user_input/user_input1
print(f"Division: {divi}")

''' Task -2 Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
'''
usr_firstname= input("enter your first name:")
usr_lastname= input("enter your last name:")

user_fullname= usr_firstname+ " " + usr_lastname

print(f"Hello, {user_fullname}!, Welcome to Python  learning program.")
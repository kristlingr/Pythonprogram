'''Task-1 Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.'''

n=input("enter any integer input:")

n=int(n)

# checking the input entered by user is even or odd in value

if n %2==0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")


'''Task-2 Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
'''
s=0
for i in range(1,51):
    s+=i
print(f"the sum of numbers from 1 to 50 is: {s}")
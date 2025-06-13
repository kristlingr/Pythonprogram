''' Task -1
Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

'''

students_data = { "Amit": 90, "Sameer": 67, "Parul": 56, "Ram": 45 }

name = input("Enter the student's name: ")

if name in students_data:
    print(f"{name}'s marks: {students_data[name]}")
else:
    print("Student not found")

'''Task-2
Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

number_list = list(range(1,11))

Extracted_list=number_list[0:5]
Extracted_list.reverse()


print(f"original list : {number_list}")
print(f"Extracted first five elements : {Extracted_list} ")
print(f"reversed extracted elements : {Extracted_list} ")



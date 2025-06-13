'''Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''


try:
    filename1 = open("sample.txt", "r")
    print("Reading file content:")

    read_lines = filename1.readlines()
    lines = 1

    for i in read_lines:
        print(f"Line {lines}: {i.strip()}")
        lines += 1

    filename1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")




''' task-2 Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''



usr_input = input("Enter text to write to the file: ")

filename2 = open("output.txt", "w")
filename2.write(usr_input+"\n")
filename2.close()
filename2 = open("output.txt", "r")
print(f"data successfully written to output.txt")

filename2.close()

filename2 = open("output.txt", "a")
add_data= input("Enter additional data text to append:")
filename2.write(add_data )
filename2.close()
print(f"data successfully appended ")

filename2.close()

filename2 = open("output.txt", "r")
print("Reading file content:")
statements = filename2.readlines()

filename2.close()

print("final content of output.txt :")
for i in statements:
    print(i.strip())







# This script is for teh purpose f sorting the number in acending order.
# Made By Malay Bhavsar

# Instruction for input file.
# Newline means new entry.
# Space entering is not entertained.

# Importing the useful module.
import os

def get_input():
    # Taking the file name as input for taking in the inputs.
    file_name = input("Enter the file-name with extension: ")
    file_open = open(f"{file_name}","r")
    # Declaring the variables.
    x = 0
    data = []
    # Running the loop for taking the input line by line.
    while x != "":
        x = file_open.readline()
        if x == "":
            break
        data.append(int(x))
    return data

def min_f(data):
    # Running the loop for finding the minimun number.
    min_num = data[0]
    for i in range(len(data)-1):
        if data[i+1] < min_num:
            min_num = data[i+1]
    return min_num

def max_f(data):
    # Running the loop for finding the maximum number.
    max_num = data[0]
    for j in range(len(data)):
        if data[j+1] > max_num:
            max_num = data[j+1]
        return max_num

def sort():
    # Getting the input ready.
    data = get_input()
    # Declaring the variable.
    new_data = []
    # Running the loop,finding the minimum number, removing it from old list and adding it to new list.
    while len(data) != 0:
        x = min_f(data)
        data.pop(data.index(x))
        new_data.append(x)
    return new_data
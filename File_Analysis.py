# This is the python code for analysing any text file.
# It takes the fle as input and then generate an output detail report.
# Only *.txt files

# Developed By Malay Bhavsar
# Version : 1

# Importing modules
import os

# Taking the files as input and reading data.
file_name = input("Enter the File-Name: ")
file_data = open(f"{file_name}","r")
msg = file_data.read()

# Defining some variables.
capital_alpha_ls = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
small_alpha_ls = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
            "o","p","q","r","s","t","u","v","w","x","y","z"]
num_ls = ["0","1","2","3","4","5","6","7","8","9"]
sp_char_ls = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","[","]",":",";",'"',"'",
            "<",">",",",".","?","/"," "]
c_alpha = s_alpha = num = sp = und = 0

# Processing the input.
for i in range(len(msg)):
    if msg[i] in capital_alpha_ls:
        c_alpha += 1
    elif msg[i] in small_alpha_ls:
        s_alpha += 1
    elif msg[i] in num_ls:
        num += 1
    elif msg[i] in sp_char_ls:
        sp += 1
    else:
        und += 1

# Writing the details of file to an output file.
detail_file = open(f"detail_{file_name}","w")
detail_file.write(f"File-name: {file_name}\n")
detail_file.write(f"Total length of file: {len(msg)}\n")
detail_file.write(f"Number of capital letters: {c_alpha}\n")
detail_file.write(f"Number of small letters: {s_alpha}\n")
detail_file.write(f"Number of numerics: {num}\n")
detail_file.write(f"Number of special character: {sp}\n")
detail_file.write(f"Number of undefined character: {und}\n")
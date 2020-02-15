# This is a encryption algorithm which works on a simple key.
# [Log]: Code improved for efficiency. Dt.05-02-2020

# Importing module
import os

# Taking the message file as input(! With extension !)
file_name = input("Enter Filename: ")
file_data = open(f"{file_name}","r")
msg = file_data.read()

# Taking the key as input.
key = int(input("Enter the Numeric key: "))

# Defining the variable.
alpha_ls = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j",
            "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num_ls = ["0","1","2","3","4","5","6","7","8","9"]
sp_char_ls = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","[","]",":",";",'"',"'",
                "<",">",",",".","?","/"]
cipher = []

# Now processing the text to cipher.
for i in range(len(msg)):
    j = 0
    # For Upper and Lower case alphabets.
    if msg[i] in alpha_ls:
        j = alpha_ls.index(msg[i]) + key
        j = j % 52
        cipher.append(alpha_ls[j])

    # For numbers.
    elif msg[i] in num_ls:
        j = num_ls.index(msg[i]) + key
        j = j % 10
        cipher.append(num_ls[j])

    # For Special Characters.
    elif msg[i] in sp_char_ls:
        j = sp_char_ls.index(msg[i]) + key
        j = j % 28
        cipher.append(sp_char_ls[j])

    # Lastly for undefined character, let it be same.
    else:
        cipher.append(msg[i])
# Writing the cipher text to a external newly create file.
cipher_file = open(f"cipher_{file_name}","w")
for k in range(len(cipher)):
    cipher_file.write(cipher[k])
print("Encryption Sucessfull :)")
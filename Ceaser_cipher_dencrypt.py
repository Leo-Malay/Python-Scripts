# This is a Ceaser Dencryption algorithm which works on a simple key.
# [Log]: Code improved for efficiency. Dt.05-02-2020

# Importing module
import os

# Taking the cipher file as input(! With extension !)
file_name = input("Enter Cipher Filename: ")
file_data = open(f"{file_name}","r")
cipher = file_data.read()

# Taking the key as input.
key = int(input("Enter the Numeric key: "))

# Defining the variable.
alpha_ls = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j",
            "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num_ls = ["0","1","2","3","4","5","6","7","8","9"]
sp_char_ls = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","[","]",":",";",'"',"'",
                "<",">",",",".","?","/"]
msg = []

# Now processing the text to cipher.
for i in range(len(cipher)):
    j = 0
    # For Upper and Lower case alphabets.
    if cipher[i] in alpha_ls:
        j = alpha_ls.index(cipher[i]) - key
        j = j % 52
        if j < 0:
            j += 52
        msg.append(alpha_ls[j])

    # For numbers.
    elif cipher[i] in num_ls:
        j = num_ls.index(cipher[i]) - key
        j = j % 10
        if j < 0:
            j += 10
        msg.append(num_ls[j])

    # For Special Characters.
    elif cipher[i] in sp_char_ls:
        j = sp_char_ls.index(cipher[i]) - key
        j = j % 28
        if j < 0:
            j += 28
        msg.append(sp_char_ls[j])

    # Lastly for undefined character, let it be same.
    else:
        msg.append(cipher[i])
# Writing the cipher text to a external newly create file.
msg_file = open(f"Plain_{file_name}","w")
for k in range(len(msg)):
    msg_file.write(msg[k])
print("Dencryption Sucessfull :)")
# This python script generally reads, write, modifys file.
# By Malay @ 2020

#           ! - Warning - ! 
# Must understand the scripts written and then consider modifing it to meet requirement.
# Must have latest python installed on your system.

# Importing the modules.
import os

# To check if the file exist.
def does_file_exist(path):
    if os.path.exists(path):
        return True
    else:
        return False

# To read file and return string.
def read_file_string(path):
    if does_file_exist(path) == True:
        file = open(f"{path}","r")
        data = file.read()
        file.close()
        return data
    else:
        return 0

# To read file and return list.
def read_file_list(path):
    if does_file_exist(path) == True:
        file = open(f"{path}","r")
        data = file.read()
        file.close()
        data = list(data.split(" "))
        return data
    else:
        return 0

# Write to file and by passing string.
def write_file_string(path,data_str):
    if does_file_exist(path) == True:
        file = open(f"{path}","a")
    else:
        file = open(f"{path}","w")
    file.write(data_str)
    file.close()

# Write to file and by passing list.
def write_file_list(path,data_list):
    if does_file_exist(path) == True:
        file = open(f"{path}","a")
    else:
        file = open(f"{path}","w")
    for i in range(len(data_list)):
        file.write(data_list[i])
    file.close()

def delete_file(path):
    if does_file_exist(path) == True:
        os.remove(path)
        return True
    else:
        return False

### Testing snipets ### {To demonstrate the use of each function.}
#write_file_list("./list.txt",['a','b','c','d','e','f'])
#write_file_list("./string.txt","ghijk")
#print(read_file_string("./list.txt"))
#print(read_file_list("./string.txt"))
#print(delete_file('./list.txt'))
#print(delete_file('./string.txt'))
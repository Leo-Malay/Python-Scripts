# This python script is of ceaser Algorithm.

def ceaser_encrypt():
    # Declaring the variables.
    new_data = []
    alpha_ls = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
                'W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
                's','t','u','v','w','x','y','z']
    # Taking the input.
    data = input("Enter your data: ")
    key = int(input("Enter your key: "))
    key %= 52
    len_data = len(data)
    # Now messing with the data.
    for i in range(len_data):
        if data[i] in alpha_ls:
            j = alpha_ls.index(data[i])
            j += key
            while j > 52:
                j -= 52
            new_data.append(alpha_ls[j])
        else:
            new_data.append(data[i])
    print(new_data)

def ceaser_dencrypt():
    # Declaring the variables.
    new_data = []
    alpha_ls = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
                'W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
                's','t','u','v','w','x','y','z']
    # Taking the input.
    data = input("Enter your data: ")
    key = int(input("Enter your key: "))
    key %= 62
    len_data = len(data)
    # Now messing with the data.
    for i in range(len_data):
        if data[i] in alpha_ls:
            j = alpha_ls.index(data[i])
            j -= key
            while j < 0:
                j += 52
            new_data.append(alpha_ls[j])
        else:
            new_data.append(data[i])
    print(new_data)
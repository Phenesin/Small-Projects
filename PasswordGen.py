import random
print("Welcome to password generator")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
no_characters=int(input("How many characters would you like to have in your password? \n"))
no_nos=int(input("How many numbers would you like to be there in the password? \n"))
no_symbols=int(input("How many symbols would you like to be there in the password?\n"))
print("\n")
password=""
password_list=[]

#basic idea for password generation

for char1 in range(1,no_characters+1):
    random_char1=random.choice(letters)
    password+=random_char1
for char2 in range(1,no_nos+1):
    random_char2=random.choice(numbers)
    password+=random_char2
for char3 in range(1,no_symbols+1):
    random_char3=random.choice(symbols)
    password+=random_char3

#advanced idea for password generation

for char1 in range(1,no_characters+1):
    random_char1=random.choice(letters)
    password_list.append(random_char1)
for char2 in range(1,no_nos+1):
    random_char2=random.choice(numbers)
    password_list.append(random_char2)
for char3 in range(1,no_symbols+1):
    random_char3=random.choice(symbols)
    password_list.append(random_char3)
random.shuffle(password_list)
print("Your generated password is:","".join(password_list)) #join is used to combine elements to form a string given as "the way you want to seperate the elements".join(variable name)



import secrets
import string

#create the entire list of characters we'll use
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
all_characters = letters + digits + special_chars

#set your password length
print("Enter how many characters you want for the password : ")
pwd_length = int(input())

# generate the password as a string
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(all_characters))

print(pwd)
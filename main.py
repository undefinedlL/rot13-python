import pyperclip
import string
import re

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase

def translate_char(letters, character):
    return letters[(letters.find(character) + 13) % 26]

while True: 
    # get a message from a user
    message = input("\nEnter a message to encrypt/decrypt (EN)\nor 'q' to exit\n>>>  ").strip()
    
    if message.lower() == "q":
        break # stop the program
    
    result = ''
    
    # translate the message
    for char in message:
        if char.isupper():
            result += translate_char(uppercase_letters, char)
        elif char.islower():
            result += translate_char(lowercase_letters, char)
        else:
            result += char
    
    print("\nThe final message is: ")
    print(result)
    
    pyperclip.copy(result)
    print("(Copied to clipboard)")
    
    answer = input("=========================\n"
                "Do you want to continue? (y/n): \n"
                ">  ").strip()
    
    if answer.lower() == 'y':
        continue
    
    break
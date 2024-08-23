import random
import pyperclip
import os

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
simbols = ['!','<','>','@','#','$','%','&','*','(','=',')', '-', '+','[',']','.',',','"',"'"]
lists = [letters, numbers, simbols]
min_length = 32

def main():
    password = ''
    for _ in range(min_length):
        random_list = random.choice(lists)
        random_element = random.choice(random_list)
        password += str(random_element)
    os.system("cls")
    print(f"Generated password sucessfully!")
    print(f"Copied to clipboard.")
    pyperclip.copy(password)

main()

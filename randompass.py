import random
import platform
import pyperclip
import os

operacionalSystem = platform.system()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
simbols = ['!','<','>','@','#','$','%','&','*','(','=',')', '-', '+','[',']','.',',','"',"'"]
lists = [letters, numbers, simbols]

def main(passwordLenght):
            password = ''
            for _ in range(passwordLenght):
                random_list = random.choice(lists)
                random_element = random.choice(random_list)
                password += str(random_element)
            pyperclip.copy(password)

if operacionalSystem == "Windows":
    os.system("cls")
else:
    os.system("clear")

while True:
    try:
        print("Digite o Número de caracteres da senha\n(Recomendado 16+)\n\n")
        lenght = int(input("> "))
        if lenght < 8:
              if operacionalSystem == "Windows":
                os.system("cls")
                print("A senha deve ter pelo menos 8 caracteres.")
              else:
                   os.system("clear")
                   print("A senha deve ter pelo menos 8 caracteres.")
        else:
            main(lenght)
        break
    except ValueError:
        if operacionalSystem == "Windows":
            os.system("cls")
            print("Por favor, digite um número inteiro.\n")
        else:
            os.system("clear")
            print("Por favor, digite um número inteiro.\n")
import pyautogui
import time
import keyboard  # Biblioteca para detectar eventos de teclado

time.sleep(5)
print("Iniciando script!\nAperte 'Backspace' para encerrar o programa.")

while True:
    if keyboard.is_pressed('backspace'):  # Verifica se a tecla Backspace foi pressionada
        print("Tecla 'Backspace' detectada. Encerrando o programa...")
        break
    pyautogui.click()  # Realiza o clique no local atual

print("Programa encerrado.")

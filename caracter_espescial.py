#como usar caracter especial 
import pyperclip
import pyautogui
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')


escrever_frase('olá, bom dia, fiz essa automação de teste espero que goste ')
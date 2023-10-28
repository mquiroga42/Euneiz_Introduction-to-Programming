"""
Main file of the program.
"""

# Importación de módulos necesarios
import os
import time
import pyfiglet
from simple_term_menu import TerminalMenu

# Función para mostrar el menú principal
def menu():
    """
    Function that displays the program's main menu.
    """
    pasword_configured = False
    password = ""
    dictionary = ""
    content = ""

    while True:
        os.system("clear")
        print(pyfiglet.figlet_format("Menu", font="big", justify="center"))
        # Opciones del menú
        options = [ "[1] Brute Force",
                    "[2] Password to search",
                    "[3] Configure Library #If not configured slowattack",
                    "[4] Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        # Acciones del menú
        if menu_entry_index == 0:
            if pasword_configured:
                if dictionary:
                    for word in content:
                        if word == password:
                            print(f"Password found: {password}")
                            time.sleep(10)
                            break
                    else:
                        print("Password not found")
                        time.sleep(1)
                else:
                    print("The dictionary is not loaded. Please configure the dictionary first.")
                    time.sleep(1)
            else:
                print("You must configure a password to search before starting the attack.")
                time.sleep(1)
        if menu_entry_index == 1:
            while True:
                password = input("Add the password to search: ")
                if len(password) == 5:
                    pasword_configured = True
                    print("The password has been configured correctly")
                    time.sleep(0.5)
                    break
                else:
                    print("Enter a 5-character password")
                    time.sleep(0.5)
        
        if menu_entry_index == 2:
            while True:
                dictionary_tosearch = input("Add the dictionary name: ")
                try:
                    with open(dictionary_tosearch, "r", encoding="utf-8") as dictionary:
                        content = dictionary.read().split()
                        if content:
                            print("Dictionary loaded successfully.")
                            time.sleep(0.5)
                            break
                except FileNotFoundError:
                    print("The dictionary does not exist.")
                    time.sleep(0.5)
                    break
        if menu_entry_index == 3:
            break

# Función principal del programa
def main():
    """
    Main function of the program.
    """
    os.system("clear")
    print(pyfiglet.figlet_format("Euneiz", font="big", justify="center"))
    time.sleep(0.5)
    os.system("clear")
    print(pyfiglet.figlet_format("Project:\nBrute Force", font="big", justify="center"))
    time.sleep(0.5)
    menu()

# Punto de entrada principal del programa
if __name__ == "__main__":
    main()

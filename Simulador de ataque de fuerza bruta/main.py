"""
Main file of the program.
"""
import os
import time
import pyfiglet
from simple_term_menu import TerminalMenu

def menu():
    """
    Function that displays the program's main menu.
    """
    pasword_configured = False
    password = ""
    dictionary = ""
    while True:
        os.system("clear")
        print(pyfiglet.figlet_format("Menu", font="big", justify="center"))
        # Menu Options
        options = [ "[1] Brute Force",
                    "[2] Password to search",
                    "[3] Configure Library #Ifnotconfigured slowattack",
                    "[4] Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        # Menu Actions
        if menu_entry_index == 0:
            if pasword_configured:
                if dictionary:
                    for password_attempt in dictionary:
                        if password_attempt == password:
                            print("Password found.")
                            time.sleep(1)
                            break
                else:
                    print("The dictionary is not loaded. Please configure the dictionary first.")
                    time.sleep(1)
            else:
                print("You must configure a password to search before starting the attack.")
                time.sleep(1)
        if menu_entry_index == 1:
            while True:
                password = input("Añade la contraseña a buscar: ")
                if len(password) == 5:
                    pasword_configured = True
                    break
        if menu_entry_index == 2:
            while True:
                dictionary_tosearch = input("Añade el nombre del diccionario: ")
                try:
                    with open(dictionary_tosearch, "r", encoding="utf-8") as dictionary:
                        content = dictionary.read()
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

if __name__ == "__main__":
    main()

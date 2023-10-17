"""
Main file of the program.
"""
import os
import time
import pyfiglet
from simple_term_menu import TerminalMenu
from password import generate_password, generate_password_list

def main_menu():
    """
    Function that displays the program's main menu.
    """
    while True:
        os.system("clear")
        print(pyfiglet.figlet_format("Menu", font="big", justify="center", width=100))
        # Menu Options
        options = ["[1] Password Generator", "[2] Dictionary Generator", "[3] Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        # Menu Actions
        if menu_entry_index == 0:
            print(generate_password())
        if menu_entry_index == 1:
            generate_password_list()
        if menu_entry_index == 2:
            return

def main():
    """
    Main function of the program.
    """
    os.system("clear")
    print(pyfiglet.figlet_format("Euneiz", font="big", justify="center", width=100))
    time.sleep(0.5)
    os.system("clear")
    print(pyfiglet.figlet_format("Project:\nPassword Generator", font="big", justify="center", width=100))
    time.sleep(0.5)
    main_menu()

if __name__ == "__main__":
    main()

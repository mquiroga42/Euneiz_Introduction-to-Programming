"""
Main file of the program.
"""

# Importación de módulos necesarios
import os
import time
import pyfiglet
from simple_term_menu import TerminalMenu
from password import generate_password, generate_password_list

# Función para mostrar el menú principal
def main_menu():
    """
    Function that displays the program's main menu.
    """
    while True:
        os.system("clear")
        print(pyfiglet.figlet_format("Menu", font="big", justify="center", width=100))
        # Opciones del menú
        options = [ "[1] Automatic Password Generator",
                    "[2] Dictionary Generator",
                    "[3] Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        # Acciones del menú
        if menu_entry_index == 0:
            print(generate_password())
        if menu_entry_index == 1:
            generate_password_list()
        if menu_entry_index == 2:
            return

# Función principal del programa
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

# Punto de entrada principal del programa
if __name__ == "__main__":
    main()

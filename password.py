"""
password.py: Este módulo proporciona funciones para generar contraseñas.
Incluye funciones para generar contraseñas aleatorias con diferentes configuraciones.
"""
import os
import string
import random
import pyfiglet
from simple_term_menu import TerminalMenu
from download import download_dictionary

class PasswordConfig:
    """
    Class that contains the configuration for generating passwords.

    Attributes:
    length (int): The length of the password.
    upper_case (bool): If the password should include uppercase letters.
    lower_case (bool): If the password should include lowercase letters.
    numbers (bool): If the password should include numbers.
    symbols (bool): If the password should include symbols.

    """
    def __init__(self, length=12, upper_case=True, lower_case=True, numbers=True, symbols=True):
        self.length = length
        self.upper_case = upper_case
        self.lower_case = lower_case
        self.numbers = numbers
        self.symbols = symbols

def password_config_menu(config):
    """
    Menu for configuring the password.
    """
    

def generate_password(config):
    """
    Generate a random password.

    Args:
    config (PasswordConfig): The configuration for the password to generate.

    Returns:
    str: The generated password.

    """
    os.system("clear")
    print(pyfiglet.figlet_format("Password", font="slant"))
    character_list = ""
    if config.upper_case:
        character_list += string.ascii_uppercase
    if config.lower_case:
        character_list += string.ascii_lowercase
    if config.numbers:
        character_list += string.digits
    if config.symbols:
        character_list += string.punctuation
    return ''.join(random.choice(character_list) for _ in range(config.length))

def generate_password_list(main_menu):
    """
    Generate a list of random passwords.
    Args:
    None
    Returns:
    None
    """
    size = 1
    while True:
        os.system("clear")
        print(pyfiglet.figlet_format("Dictionary Generator", font="big"))
        # Menu Options
        options = ["[1] Generate Dictionary", "[2] Dictionary List Size (" + str(size) + ")", "[3] Password Configuration", "[4] Back"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        # Menu Actions
        if menu_entry_index == 0:
            config = PasswordConfig()
            word_list = [generate_password(config) for _ in range(size)]
            download_dictionary(word_list, "test")
            break
        if menu_entry_index == 1:
            while True:
                try:
                    size = int(input("Number of passwords to generate: "))
                    break
                except ValueError:
                    print("Invalid input")
        if menu_entry_index == 2:
            continue
        if menu_entry_index == 3:
            return

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

config = PasswordConfig()

def password_config_menu():
    """
    Menu for configuring the password.
    Args:
    None
    Returns:
    PasswordConfig: The configuration for the password.
    """
    while True:
        os.system("clear")
        print(pyfiglet.figlet_format("Password Configurator", font="big"))
        # Menu Options
        options = [ "[1] SetLengthPassword (" + str(config.length) + ")",
                    "[2] UpperCase (" + str(config.upper_case) + ")",
                    "[3] LowerCase (" + str(config.lower_case) + ")",
                    "[4] Numbers (" + str(config.numbers) + ")",
                    "[5] Symbols (" + str(config.symbols) + ")",
                    "[6] Back"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        # Menu Actions
        if menu_entry_index == 0:
            while True:
                try:
                    config.length = int(input("Length of the password: "))
                    break
                except ValueError:
                    print("Invalid input")
        if menu_entry_index == 1:
            config.upper_case = not config.upper_case
        if menu_entry_index == 2:
            config.lower_case = not config.lower_case
        if menu_entry_index == 3:
            config.numbers = not config.numbers
        if menu_entry_index == 4:
            config.symbols = not config.symbols
        if menu_entry_index == 5:
            return config

def generate_password():
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

def generate_password_list():
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
        options = [ "[1] Generate Dictionary",
                    "[2] Dictionary List Size (" + str(size) + ")",
                    "[3] Password Configuration",
                    "[4] Back"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        # Menu Actions
        if menu_entry_index == 0:
            word_list = [generate_password() for _ in range(size)]
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
            config = password_config_menu()
        if menu_entry_index == 3:
            return

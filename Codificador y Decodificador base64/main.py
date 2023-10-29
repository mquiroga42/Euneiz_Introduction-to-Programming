"""
Main file of the program.
"""

import base64
import os
import time
import pyfiglet
from simple_term_menu import TerminalMenu

def decode_base64(string_codificado):
    """
    Function to decode a string in base64.
    Args:
    string_codificado (str): The string to decode.
    Returns:
    str: The decoded string.
    """
    try:
        string_decodificado = base64.b64decode(string_codificado).decode('utf-8')
        return string_decodificado
    except Exception as e:
        return f"Error: {e}"

def encode_base64(string_decodificado):
    """
    Function to encode a string in base64.
    Args:
    string_decodificado (str): The string to encode.
    Returns:
    str: The encoded string.
    """
    try:
        string_codificado = base64.b64encode(string_decodificado.encode('utf-8')).decode('utf-8')
        return string_codificado
    except Exception as e:
        return f"Error: {e}"

def menu():
    """
    Function that displays the program's main menu.
    Args:
    None
    Returns:
    None
    """
    string_decodificado = ""
    string_codificado = ""
    while True:
        os.system("clear")
        print(pyfiglet.figlet_format("Menu", font="big", justify="center"))
        options = ["[1] Decode string in base64", "[2] Encode string in base64", "[3] Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if menu_entry_index == 0:
            string_codificado = input("Add the string to decode: ")
            if string_codificado:
                string_decodificado = decode_base64(string_codificado)
                print(f"Decoded string: {string_decodificado}")
                input("Press Enter to continue...")
            else:
                print("You must provide a string to decode")
                time.sleep(1)
        elif menu_entry_index == 1:
            string_decodificado = input("Add the string to encode: ")
            if string_decodificado:
                string_codificado = encode_base64(string_decodificado)
                print(f"Encoded string: {string_codificado}")
                input("Press Enter to continue...")
            else:
                print("You must provide a string to encode")
                time.sleep(1)
        elif menu_entry_index == 2:
            break

def main():
    """
    Main function of the program.
    Args:
    None
    Returns:
    None
    """
    os.system("clear")
    print(pyfiglet.figlet_format("Euneiz", font="big", justify="center", width=100))
    time.sleep(0.5)
    os.system("clear")
    print(pyfiglet.figlet_format("Project:\nPassword Generator", font="big", justify="center", width=100))
    time.sleep(0.5)
    menu()

if __name__ == "__main__":
    main()

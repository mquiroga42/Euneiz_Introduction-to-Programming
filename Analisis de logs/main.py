"""
Main file of the program.
"""
import os
import re
import time
import datetime
import pyfiglet
from simple_term_menu import TerminalMenu

def get_log_file(service):
    """
    Function that returns the log file of the specified service.
    Parameters:
        service (str): Name of the service.
    Returns:
        str: Name of the log file.
    """
    if service == "SSH":
        return "auth.log"
    return ""

def scan_logs(service):
    """
    Function that scans the logs of the specified service and returns a log entry that meets the criteria.
    """
    log_file = get_log_file(service)
    with open(log_file, 'r', encoding="utf-8") as file:
        log_entries = file.readlines()

    brute_force_attempts = {}

    for entry in log_entries:
        match = re.search(r'Failed password for (.+) from (\d+\.\d+\.\d+\.\d+)', entry)
        if match:
            _, ip_address = match.group(1), match.group(2)
            now = datetime.datetime.now()
            print(entry)
            if ip_address in brute_force_attempts:
                brute_force_attempts[ip_address]["attempts"] += 1
            else:
                brute_force_attempts[ip_address] = {}
                brute_force_attempts[ip_address]["start_time"] = now
                brute_force_attempts[ip_address]["log"] = entry
                brute_force_attempts[ip_address]["attempts"] = 1
        brute_force = any
        brute_force = [entry for entry in brute_force_attempts.values() if entry["attempts"] >= 10]
        if brute_force:
            return brute_force_attempts
    return None

def main_menu():
    """
    Function that displays the program's main menu.
    """
    service = ""
    while True:
        os.system("clear")
        print(pyfiglet.figlet_format("Menu", font="big", justify="center"))
        # Menu Options
        options = [ "[1] Check Logs - Brute Force Attacks",
                    "[-] Select Service (SSH) Disabled",
                    "[3] Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        # Menu Actions
        if menu_entry_index == 0:
            if service != "":
                print(scan_logs(service))
                input("Press Enter to continue...")
            else:
                print("You must select a service first.")
                time.sleep(1)
        if menu_entry_index == 1:
            service = "SSH"
        if menu_entry_index == 2:
            return

def main():
    """
    Main function of the program.
    """
    os.system("clear")
    print(pyfiglet.figlet_format("Euneiz", font="big", justify="center"))
    time.sleep(0.5)
    os.system("clear")
    print(pyfiglet.figlet_format("Project:\nLogs analitics", font="big", justify="center", width=100))
    time.sleep(0.5)
    main_menu()

if __name__ == "__main__":
    main()

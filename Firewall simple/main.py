"""
Main file of the program.
"""
import os
import time
import pyfiglet
from scapy.sendrecv import sniff
from scapy.all import IP
from simple_term_menu import TerminalMenu

blocked_list = {
    "192.168.1.10": ["ICMP", "TCP"],
    "192.168.1.11": ["UDP", "HTTP"]
}

def handle_packet(packet):
    """
    Function that handles a packet.
    """
    if IP in packet and packet[IP].src in blocked_list:
        src_ip = packet[IP].src
        packet_type = packet[IP].proto
        if packet_type == 1:
            packet_type = "ICMP"
        elif packet_type == 6:
            packet_type = "TCP"
        elif packet_type == 17:
            packet_type = "UDP"
        if packet_type in blocked_list[src_ip]:
            print("Blocked packet from " + src_ip + " of type " + packet_type)
            return

def main_menu():
    """
    Function that displays the program's main menu.
    """
    while True:
        os.system("clear")
        print(pyfiglet.figlet_format("Menu", font="big", justify="center"))
        # Menu Options
        options = [ "[1] Configure Firewall",
                    "[2] Start Firewall",
                    "[3] Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        # Menu Actions
        if menu_entry_index == 0:
            print("Configure Firewall")
        elif menu_entry_index == 1:
            sniff(prn=handle_packet)
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
    print(pyfiglet.figlet_format("Project:\nFirewall Simple", font="big", justify="center"))
    time.sleep(0.5)
    main_menu()

if __name__ == "__main__":
    main()

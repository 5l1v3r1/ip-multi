import os
from os import system, name
import sys
import ctypes
import time
import colorama
from colorama import Fore

if os.name == "nt":
    OS = "WINDOWS"

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    ctypes.windll.kernel32.SetConsoleTitleW("github.com/purelxw")
    clear()
    if len(sys.argv) < 2:
        os.system("clear || cls")
        sys.stdout.write(f'''{Fore.RESET}


{Fore.LIGHTBLACK_EX}      ┬┌─┐     {Fore.RED}┌┬┐┬ ┬┬ ┌┬┐┬
{Fore.LIGHTBLACK_EX}      │├─┘ ─── {Fore.RED}││││ ││  │ │
{Fore.LIGHTBLACK_EX}      ┴┴       {Fore.RED}┴ ┴└─┘┴─┘┴ ┴ {Fore.LIGHTWHITE_EX} Author: purelxw
    
{Fore.LIGHTBLACK_EX}   [{Fore.RED}1{Fore.LIGHTBLACK_EX}] ICMP Ping
{Fore.LIGHTBLACK_EX}   [{Fore.RED}2{Fore.LIGHTBLACK_EX}] IP lookup
{Fore.LIGHTBLACK_EX}   [{Fore.RED}3{Fore.LIGHTBLACK_EX}] TCP Port Scan
    '''+Fore.RESET)

    print('')
    choice = input(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}?{Fore.LIGHTBLACK_EX}] Option: {Fore.LIGHTWHITE_EX}")

    if choice == "1":
        print(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}!{Fore.LIGHTBLACK_EX}] {Fore.GREEN}Forwarding...{Fore.RESET}")
        time.sleep(0.3)
        import icmp
    elif choice == "2":
        print(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}!{Fore.LIGHTBLACK_EX}] {Fore.GREEN}Forwarding...{Fore.RESET}")
        time.sleep(0.3)
        import lookup
    elif choice == "3":
        print(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}!{Fore.LIGHTBLACK_EX}] {Fore.GREEN}Forwarding...{Fore.RESET}")
        time.sleep(0.3)
        import port
    else:
        print(f"{Fore.LIGHTBLACK_EX} [{Fore.RED}!{Fore.LIGHTBLACK_EX}] {Fore.RED}Invalid option, please try again...{Fore.RESET}")
        time.sleep(1)
        main()

main()

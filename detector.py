import sys
from utils import load_patterns, detect_sqli, log_attack
import colorama
from colorama import Fore, Style

# Initialize colorama (important for Windows)
colorama.init(autoreset=True)
 
patterns = load_patterns()

def main():
    print(f"{Fore.YELLOW}=== SQL Injection Detection Tool ==={Style.RESET_ALL}")
    print("Type 'exit' to quit.\n")

    while True:
        payload = input("Enter input (simulated payload): ").strip()
        if payload.lower() == 'exit':
            print(f"{Fore.YELLOW}Exiting the tool.{Style.RESET_ALL}")
            break

        ip = "127.0.0.1"
        endpoint = "/test"

        matched_pattern = detect_sqli(payload, patterns)
        if matched_pattern:
            print(f"{Fore.RED}[!] SQL Injection Detected!{Style.RESET_ALL} Pattern matched: {Fore.RED}{matched_pattern}{Style.RESET_ALL}\n")
            log_attack(ip, endpoint, payload, matched_pattern)
        else:
            print(f"{Fore.GREEN}[+] Clean input. No SQLi detected.{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main()

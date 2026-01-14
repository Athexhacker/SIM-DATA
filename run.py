import requests
import time
import sys
import os
from datetime import datetime
import json
from colorama import init, Fore, Style, Back
from pyfiglet import Figlet
import threading
import random

# Initialize colorama for Windows compatibility
init(autoreset=True)

class SIMDatabaseScanner:
    def __init__(self):
        self.api_url = "https://pak-sim-info.ftgmhacks.workers.dev"
        self.version = "ATHEX SIM DB v3.0"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (ATHEX SIM Database Scanner/3.0)'
        })
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def animate_text(self, text, delay=0.03, color=Fore.CYAN):
        """Animate text printing with color"""
        for char in text:
            print(color + char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def show_ascii_banner(self):
        """Display animated ASCII banner"""
        self.clear_screen()
        
        # ASCII Banner with colors
        banner = f"""{Fore.CYAN}
    █████╗ ████████╗██╗  ██╗███████╗██╗  ██╗   ███████╗  ██████╗  ██████╗ 
   ██╔══██╗╚══██╔══╝██║  ██║██╔════╝╚██╗██╔╝   ██╔════╝  ██╔══██╗ ██╔══██╗
   ███████║   ██║   ███████║█████╗   ╚███╔╝    ███████╗  ██║  ██║ ██████╔╝ 
   ██╔══██║   ██║   ██╔══██║██╔══╝   ██╔██╗    ╚════██║  ██║  ██║ ██╔══██╗
   ██║  ██║   ██║   ██║  ██║███████╗██╔╝ ██╗   ███████║  ██████╔╝ ██████╔╝
   ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚══════╝  ╚═════╝  ╚═════╝ 
                          TEAM ATHEX
{Style.RESET_ALL}
"""
        
        for line in banner.split('\n'):
            print(line)
            time.sleep(0.05)
        
        # Animated subtitle
        subtitle = "CYBER INTELLIGENCE DATABASE SCANNER"
        print(Fore.YELLOW + "═" * 60)
        self.animate_text(subtitle, delay=0.02, color=Fore.MAGENTA)
        print(Fore.YELLOW + "═" * 60 + "\n")
    
    def show_scanning_animation(self):
        """Show scanning animation"""
        frames = [
            f"{Fore.CYAN}[{Fore.GREEN}■{Fore.CYAN}□□□□□□□□□] Scanning...",
            f"{Fore.CYAN}[{Fore.GREEN}■■{Fore.CYAN}□□□□□□□□] Connecting...",
            f"{Fore.CYAN}[{Fore.GREEN}■■■{Fore.CYAN}□□□□□□□] Querying API...",
            f"{Fore.CYAN}[{Fore.GREEN}■■■■{Fore.CYAN}□□□□□□] Analyzing...",
            f"{Fore.CYAN}[{Fore.GREEN}■■■■■{Fore.CYAN}□□□□□] Processing...",
            f"{Fore.CYAN}[{Fore.GREEN}■■■■■■{Fore.CYAN}□□□□] Decrypting...",
            f"{Fore.CYAN}[{Fore.GREEN}■■■■■■■{Fore.CYAN}□□□] Validating...",
            f"{Fore.CYAN}[{Fore.GREEN}■■■■■■■■{Fore.CYAN}□□] Finalizing...",
            f"{Fore.CYAN}[{Fore.GREEN}■■■■■■■■■{Fore.CYAN}□] Completing...",
            f"{Fore.CYAN}[{Fore.GREEN}■■■■■■■■■■{Fore.CYAN}] Done!"
        ]
        
        for frame in frames:
            sys.stdout.write('\r' + ' ' * 100)
            sys.stdout.write('\r' + frame)
            sys.stdout.flush()
            time.sleep(0.2)
        print("\n")
    
    def show_matrix_effect(self, duration=3):
        """Show Matrix-style effect"""
        chars = "01█▓▒░"
        width = 60
        height = 10
        
        end_time = time.time() + duration
        while time.time() < end_time:
            self.clear_screen()
            for _ in range(height):
                line = ''.join(random.choice(chars) for _ in range(width))
                print(Fore.GREEN + line)
            time.sleep(0.1)
    
    def get_sim_info(self, phone_number):
        """Fetch SIM information from API"""
        try:
            start_time = time.time()
            response = self.session.get(f"{self.api_url}/?num={phone_number}")
            response_time = (time.time() - start_time) * 1000  # Convert to ms
            
            if response.status_code == 200:
                data = response.json()
                return data, response_time
            else:
                return None, response_time
        except Exception as e:
            print(Fore.RED + f"Error: {e}")
            return None, 0
    
    def display_results(self, data, response_time):
        """Display the results in formatted output"""
        if not data or not data.get('success'):
            print(Fore.RED + "\n✗ No records found!")
            print(Fore.YELLOW + "The specified mobile number could not be found in our database.")
            return
        
        results = data.get('data', {}).get('data', [])
        
        print(Fore.GREEN + "\n" + "═" * 60)
        print(Fore.CYAN + "📊 INTELLIGENCE REPORT")
        print(Fore.GREEN + "═" * 60)
        
        print(Fore.YELLOW + f"Query Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(Fore.YELLOW + f"Response Time: {response_time:.2f} ms")
        print(Fore.YELLOW + f"Records Found: {len(results)}")
        print(Fore.GREEN + "═" * 60 + "\n")
        
        for idx, record in enumerate(results, 1):
            print(Fore.MAGENTA + f"┌───────────────── TARGET #{idx} ─────────────────┐")
            print(Fore.CYAN + f"   👤 Name: {Fore.WHITE}{record.get('Name', 'N/A')}")
            print(Fore.CYAN + f"   📱 Mobile: {Fore.WHITE}{record.get('Mobile', 'N/A')}")
            print(Fore.CYAN + f"   🆔 CNIC: {Fore.WHITE}{record.get('CNIC', 'N/A')}")
            print(Fore.CYAN + f"   📍 Address: {Fore.WHITE}{record.get('Address', 'N/A')}")
            print(Fore.MAGENTA + f"└──────────────────────────────────────────────────┘\n")
    
    def show_main_menu(self):
        """Display main menu"""
        print(Fore.CYAN + "╔" + "═" * 58 + "╗")
        print(Fore.CYAN + "║" + Fore.YELLOW + "                    MAIN MENU                     ".center(58) + Fore.CYAN + "║")
        print(Fore.CYAN + "╠" + "═" * 58 + "╣")
        print(Fore.CYAN + "║" + Fore.GREEN + " 1. Scan Mobile Number" + " " * 36 + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.BLUE + " 2. Batch Scan (Multiple Numbers)" + " " * 26 + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.MAGENTA + " 3. View Scan History" + " " * 37 + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.YELLOW + " 4. System Information" + " " * 36 + Fore.CYAN + "║")
        print(Fore.CYAN + "║" + Fore.RED + " 5. Exit" + " " * 50 + Fore.CYAN + "║")
        print(Fore.CYAN + "╚" + "═" * 58 + "╝\n")
    
    def validate_phone(self, phone):
        """Validate Pakistani phone number"""
        if len(phone) != 11:
            return False
        if not phone.isdigit():
            return False
        # Check Pakistani mobile prefixes
        prefixes = ['03', '030', '031', '032', '033', '034', '035', '036']
        return any(phone.startswith(prefix) for prefix in prefixes)
    
    def run(self):
        """Main program loop"""
        while True:
            self.show_ascii_banner()
            self.show_main_menu()
            
            choice = input(Fore.CYAN + "Select option (1-5): " + Fore.WHITE)
            
            if choice == '1':
                self.clear_screen()
                self.show_ascii_banner()
                
                print(Fore.CYAN + "\n" + "═" * 60)
                print(Fore.YELLOW + "📱 SINGLE NUMBER SCAN")
                print(Fore.CYAN + "═" * 60)
                
                phone = input(Fore.GREEN + "\nEnter mobile number (03001234567): " + Fore.WHITE)
                
                if self.validate_phone(phone):
                    print(Fore.YELLOW + f"\nTarget: {phone}")
                    print(Fore.YELLOW + "Initiating scan...")
                    
                    # Show scanning animation
                    scan_thread = threading.Thread(target=self.show_scanning_animation)
                    scan_thread.start()
                    
                    # Fetch data
                    data, response_time = self.get_sim_info(phone)
                    
                    scan_thread.join()
                    
                    # Show results
                    self.display_results(data, response_time)
                else:
                    print(Fore.RED + "\n✗ Invalid phone number!")
                    print(Fore.YELLOW + "Please enter a valid 11-digit Pakistani mobile number.")
                
                input(Fore.CYAN + "\nPress Enter to continue..." + Fore.WHITE)
                
            elif choice == '2':
                self.clear_screen()
                self.show_ascii_banner()
                print(Fore.YELLOW + "\nBatch scanning feature coming soon!")
                input(Fore.CYAN + "\nPress Enter to continue..." + Fore.WHITE)
                
            elif choice == '3':
                self.clear_screen()
                self.show_ascii_banner()
                print(Fore.YELLOW + "\nScan history feature coming soon!")
                input(Fore.CYAN + "\nPress Enter to continue..." + Fore.WHITE)
                
            elif choice == '4':
                self.clear_screen()
                self.show_ascii_banner()
                print(Fore.CYAN + "\n" + "═" * 60)
                print(Fore.YELLOW + "🖥️ SYSTEM INFORMATION")
                print(Fore.CYAN + "═" * 60)
                print(Fore.GREEN + f"\nVersion: {self.version}")
                print(Fore.GREEN + f"Python Version: {sys.version}")
                print(Fore.GREEN + f"Platform: {sys.platform}")
                print(Fore.GREEN + f"Current Time: {datetime.now()}")
                input(Fore.CYAN + "\nPress Enter to continue..." + Fore.WHITE)
                
            elif choice == '5':
                self.clear_screen()
                print(Fore.CYAN + "\nShutting down ATHEX SIM Database Scanner...")
                print(Fore.YELLOW + "All connections terminated.")
                print(Fore.GREEN + "Goodbye!\n")
                time.sleep(2)
                break
            else:
                print(Fore.RED + "\nInvalid choice! Please select 1-5.")
                time.sleep(1)

if __name__ == "__main__":
    # Check for required packages
    try:
        from colorama import init
        from pyfiglet import Figlet
    except ImportError:
        print("Installing required packages...")
        os.system("pip install colorama pyfiglet requests")
        print("\nPackages installed. Please run the script again.")
        sys.exit(1)
    
    # Run the scanner
    scanner = SIMDatabaseScanner()
    
    try:
        scanner.run()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nProgram interrupted by user.")
        print(Fore.YELLOW + "Exiting ATHEX SIM Database Scanner...")
    except Exception as e:
        print(Fore.RED + f"\nUnexpected error: {e}")
        print(Fore.YELLOW + "Please check your internet connection and try again.")


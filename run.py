#!/usr/bin/env python3
import requests
import json
import time
import sys
import os
import random
from datetime import datetime
from threading import Thread
from queue import Queue
import textwrap

# Terminal colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    MAGENTA = '\033[95m'
    ORANGE = '\033[33m'
    PURPLE = '\033[35m'
    GRAY = '\033[90m'
    END = '\033[0m'

# Matrix-style falling characters for extra effect
def matrix_rain():
    chars = "01█▓▒░ΣΦΨΩαβγδεζηθλμξπρστυφχψω"
    width = 80
    drops = [0] * width
    
    for _ in range(50):  # Run for 50 frames
        print('\033[32m', end='')  # Green color for matrix
        for i in range(width):
            if drops[i] == 0 and random.random() > 0.975:
                drops[i] = random.randint(1, 20)
            
            if drops[i] > 0:
                print(random.choice(chars), end='')
                drops[i] -= 1
            else:
                print(' ', end='')
        print('\033[0m')
        time.sleep(0.05)

# Enhanced animated banner
def display_epic_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Phase 1: Matrix rain effect
    print(f"\n{Colors.GREEN}Initializing System...{Colors.END}")
    time.sleep(1)
    
    # Phase 2: Epic ASCII art reveal with animation
    banner_parts = [
        f"""{Colors.CYAN}
    ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗ 
    ║ ╔═╝ ║ ╔═╝ ║ ╔═╝ ║ ╔═╝ ║ ╔═╝ ║ ╔═╝ 
    ║ ╚═╗ ║ ╚═╗ ║ ╚═╗ ║ ╚═╗ ║ ╚═╗ ║ ╚═╗ 
    ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝ 
        """,
        f"""{Colors.PURPLE}
                █████╗ ████████╗██╗  ██╗███████╗██╗  ██╗",
               ██╔══██╗╚══██╔══╝██║  ██║██╔════╝╚██╗██╔╝",
               ███████║   ██║   ███████║█████╗   ╚███╔╝ ",
               ██╔══██║   ██║   ██╔══██║██╔══╝   ██╔██╗ ",
               ██║  ██║   ██║   ██║  ██║███████╗██╔╝ ██╗",
               ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝",
                    TEAM ATHEX CYBER INTELLIGENCE",
        """,
        f"""{Colors.ORANGE}{Colors.BOLD}
    
       █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█   
       █  PAKISTANI SIM DATABASE LOOKUP SYSTEM  █   
       █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█   
                                                         
             CREATED BY: ATHEX BLACK HAT TEAM                         
   ═════════════════════════════════════════════════════
        """
    ]
    
    # Animate banner reveal
    for part in banner_parts:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(part)
        time.sleep(0.8)
    
    # Final pulse animation
    pulse_colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE]
    for _ in range(3):
        for color in pulse_colors:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(banner_parts[2].replace(Colors.ORANGE, color))
            time.sleep(0.1)

def lookup_sim(number):
    """Query the SIM database API"""
    url = f"https://fam-official.serv00.net/api/database.php?number={number}"
    
    try:
        response = requests.get(url, timeout=15)
        data = response.json()
        return data, response.text  # Return both parsed and raw JSON
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": f"Network error: {str(e)}"}, None
    except json.JSONDecodeError:
        return {"success": False, "error": "Invalid response from server"}, None

def epic_loading_animation(message="ACCESSING SIM DATABASE"):
    """Enhanced loading animation with multiple effects"""
    frames = [
        ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"],
        ["◢", "◣", "◤", "◥"],
        ["◐", "◓", "◑", "◒"],
        ["⣀", "⣄", "⣤", "⣦", "⣶", "⣷", "⣿", "⡿", "⠿", "⢟", "⠟", "⡛", "⠛", "⠫", "⢋", "⠋", "⠍", "⡉", "⠉", "⠑", "⠡", "⢁"],
        ["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"],
        ["⠁", "⠂", "⠄", "⡀", "⢀", "⠠", "⠐", "⠈"]
    ]
    
    colors = [Colors.RED, Colors.ORANGE, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.PURPLE]
    
    start_time = time.time()
    while time.time() - start_time < 3:  # Run for 3 seconds
        frame_set = random.choice(frames)
        color = random.choice(colors)
        
        for i, frame in enumerate(frame_set):
            sys.stdout.write(f"\r{color}{frame} {message} [{'.' * ((i % 3) + 1)}]{' ' * 20}{Colors.END}")
            sys.stdout.flush()
            time.sleep(0.1)
    
    sys.stdout.write("\r" + " " * 60 + "\r")

def animate_text(text, delay=0.05, color=Colors.GREEN):
    """Typewriter animation for text"""
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.END}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_cool_json(json_str, indent=2):
    """Print JSON in a cool animated format with syntax highlighting"""
    try:
        data = json.loads(json_str)
        
        # Create a border
        print(f"\n{Colors.CYAN}{'╔'}{'═' * 66}{'╗'}{Colors.END}")
        
        # Print JSON header
        print(f"{Colors.CYAN}║{Colors.END} {Colors.YELLOW}{Colors.BOLD}🎯 RAW JSON RESPONSE:{Colors.END} {' ' * 40}{Colors.CYAN}║{Colors.END}")
        print(f"{Colors.CYAN}{'╠'}{'═' * 66}{'╣'}{Colors.END}")
        
        # Convert JSON to pretty string
        pretty_json = json.dumps(data, indent=indent, ensure_ascii=False)
        
        # Split into lines and animate
        lines = pretty_json.split('\n')
        for line in lines:
            # Skip empty lines
            if not line.strip():
                print(f"{Colors.CYAN}║{Colors.END}")
                continue
                
            # Syntax highlighting
            colored_line = line
            
            # Color keys (before colon)
            if ':' in line:
                key_part = line.split(':')[0]
                value_part = ':'.join(line.split(':')[1:])
                
                # Clean up key formatting
                key_part = key_part.strip()
                
                # Color based on content
                if '"' in key_part:
                    key_part = f"{Colors.GREEN}{key_part}{Colors.END}"
                elif '[' in key_part or ']' in key_part:
                    key_part = f"{Colors.PURPLE}{key_part}{Colors.END}"
                elif '{' in key_part or '}' in key_part:
                    key_part = f"{Colors.BLUE}{key_part}{Colors.END}"
                
                # Color values
                if '"' in value_part:
                    # Find quoted strings
                    import re
                    quoted_strings = re.findall(r'"[^"]*"', value_part)
                    for qs in quoted_strings:
                        colored_value = f"{Colors.CYAN}{qs}{Colors.END}"
                        value_part = value_part.replace(qs, colored_value)
                
                # Color booleans and null
                value_part = value_part.replace('true', f"{Colors.GREEN}true{Colors.END}")
                value_part = value_part.replace('false', f"{Colors.RED}false{Colors.END}")
                value_part = value_part.replace('null', f"{Colors.GRAY}null{Colors.END}")
                
                # Color numbers
                import re
                numbers = re.findall(r'\b\d+\b', value_part)
                for num in numbers:
                    value_part = value_part.replace(num, f"{Colors.YELLOW}{num}{Colors.END}")
                
                colored_line = f"{key_part}:{value_part}"
            
            # Print with border
            padded_line = colored_line.ljust(65)
            print(f"{Colors.CYAN}║{Colors.END} {padded_line} {Colors.CYAN}║{Colors.END}")
            time.sleep(0.03)
        
        # Close border
        print(f"{Colors.CYAN}{'╚'}{'═' * 66}{'╝'}{Colors.END}")
        
    except json.JSONDecodeError:
        # If not valid JSON, print raw response
        print(f"\n{Colors.RED}⚠️ Raw Response (Not valid JSON):{Colors.END}")
        print(f"{Colors.GRAY}{json_str}{Colors.END}")

def print_json_box(data, title="JSON DATA"):
    """Print JSON in a fancy box with animations"""
    json_str = json.dumps(data, indent=2, ensure_ascii=False)
    
    # Calculate box width
    max_line_length = max(len(line) for line in json_str.split('\n'))
    box_width = min(max_line_length + 4, 80)
    
    # Top border animation
    top_border = f"{Colors.CYAN}┌{'─' * (box_width-2)}┐{Colors.END}"
    for i in range(len(top_border)):
        sys.stdout.write(top_border[i])
        sys.stdout.flush()
        time.sleep(0.005)
    print()
    
    # Title with animation
    title_line = f"{Colors.CYAN}│{Colors.END} {Colors.YELLOW}{Colors.BOLD}📊 {title}{Colors.END}"
    title_line = title_line.ljust(box_width - 2) + f"{Colors.CYAN}│{Colors.END}"
    animate_text(title_line, 0.01, Colors.WHITE)
    
    # Separator
    sep_line = f"{Colors.CYAN}├{'─' * (box_width-2)}┤{Colors.END}"
    print(sep_line)
    
    # JSON content with syntax highlighting
    lines = json_str.split('\n')
    for line_num, line in enumerate(lines):
        # Syntax highlighting
        colored_line = line
        
        # Highlight keys
        if ':' in line and '"' in line.split(':')[0]:
            parts = line.split(':')
            key = parts[0]
            value = ':'.join(parts[1:])
            
            # Color key
            colored_key = f"{Colors.GREEN}{key}{Colors.END}"
            
            # Color value
            colored_value = value
            # String values
            if '"' in value:
                import re
                strings = re.findall(r'"[^"]*"', value)
                for s in strings:
                    colored_value = colored_value.replace(s, f"{Colors.CYAN}{s}{Colors.END}")
            
            # Boolean values
            colored_value = colored_value.replace('true', f"{Colors.GREEN}true{Colors.END}")
            colored_value = colored_value.replace('false', f"{Colors.RED}false{Colors.END}")
            colored_value = colored_value.replace('null', f"{Colors.GRAY}null{Colors.END}")
            
            # Number values
            import re
            numbers = re.findall(r'\b\d+\b', colored_value)
            for num in numbers:
                colored_value = colored_value.replace(num, f"{Colors.YELLOW}{num}{Colors.END}")
            
            colored_line = f"{colored_key}:{colored_value}"
        
        # Add border and padding
        padded_line = colored_line.ljust(box_width - 4)
        final_line = f"{Colors.CYAN}│{Colors.END} {padded_line} {Colors.CYAN}│{Colors.END}"
        
        # Typewriter effect for each line
        for char in final_line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.002)
        print()
    
    # Bottom border
    bottom_border = f"{Colors.CYAN}└{'─' * (box_width-2)}┘{Colors.END}"
    for char in bottom_border:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)
    print()

def display_animated_result(data, raw_json, number):
    """Display results with cool animations and JSON view"""
    print(f"\n{Colors.CYAN}{'█' * 60}{Colors.END}")
    
    # Animate header
    animate_text("▓▓▓ SIM DATABASE QUERY RESULTS ▓▓▓", 0.03, Colors.YELLOW + Colors.BOLD)
    
    print(f"{Colors.CYAN}{'─' * 60}{Colors.END}")
    
    # Phone number reveal
    print(f"{Colors.BLUE}┌─[📱 PHONE NUMBER]{Colors.END}")
    time.sleep(0.3)
    print(f"{Colors.GREEN}│ {Colors.BOLD}{number}{Colors.END}")
    
    # Query time
    print(f"{Colors.BLUE}├─[🕐 QUERY TIME]{Colors.END}")
    time.sleep(0.3)
    print(f"{Colors.CYAN}│ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.END}")
    print(f"{Colors.BLUE}├─[📊 STATUS]{Colors.END}")
    time.sleep(0.3)
    
    if data.get("success"):
        # Success animation
        success_frames = ["✓", "✔", "✅", "🎯", "🎉", "🔥"]
        for frame in success_frames:
            sys.stdout.write(f"\r{Colors.GREEN}│ {frame} QUERY SUCCESSFUL{'!' * random.randint(1, 3)}{' ' * 10}{Colors.END}")
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        
        # Animated data display
        print(f"{Colors.BLUE}├─[📋 RETRIEVED DATA]{Colors.END}")
        time.sleep(0.5)
        
        icons = ["📞", "👤", "🏢", "📍", "🏷️", "📅", "🌐", "🔢", "🆔"]
        
        for key, value in data.items():
            if key not in ["success"]:
                icon = random.choice(icons)
                # Typewriter effect for each line
                line = f"{Colors.PURPLE}│ {icon} {key.upper().replace('_', ' ')}:{Colors.END} "
                for char in line:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.01)
                
                # Value reveal with random color
                value_color = random.choice([Colors.GREEN, Colors.CYAN, Colors.YELLOW, Colors.ORANGE])
                for char in str(value):
                    sys.stdout.write(f"{value_color}{char}{Colors.END}")
                    sys.stdout.flush()
                    time.sleep(0.02)
                print()
                time.sleep(0.2)
    else:
        # Error animation
        error_frames = ["✗", "✘", "❌", "🚫", "⚠️", "💥"]
        for frame in error_frames:
            sys.stdout.write(f"\r{Colors.RED}│ {frame} QUERY FAILED{'!' * random.randint(1, 3)}{' ' * 10}{Colors.END}")
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        
        if "error" in data:
            print(f"{Colors.RED}│ 📛 ERROR: {data['error']}{Colors.END}")
        if "usage" in data:
            print(f"{Colors.YELLOW}│ 📖 USAGE: {data['usage']}{Colors.END}")
    
    if "credit" in data:
        print(f"{Colors.BLUE}├─[👨‍💻 CREDITS]{Colors.END}")
        time.sleep(0.3)
        # Credit scroll animation
        credit_text = f"│ {data['credit']}"
        for i in range(len(credit_text)):
            print(f"{Colors.GRAY}{credit_text[:i+1]}{Colors.END}", end='\r')
            time.sleep(0.05)
        print()
    
    print(f"{Colors.CYAN}{'█' * 60}{Colors.END}")
    
    # Ask user if they want to see JSON
    print(f"\n{Colors.YELLOW}🔍 Want to see the raw JSON response? (y/n): {Colors.END}", end='')
    show_json = input().strip().lower()
    
    if show_json == 'y':
        print("\n" + "="*70)
        animate_text("🔄 LOADING JSON VIEWER...", 0.03, Colors.CYAN)
        print("="*70)
        
        # Display JSON in cool format
        if raw_json:
            print_cool_json(raw_json)
            time.sleep(1)
            
            # Also show in box format
            print(f"\n{Colors.YELLOW}📦 Want to see formatted JSON box? (y/n): {Colors.END}", end='')
            show_box = input().strip().lower()
            
            if show_box == 'y':
                print("\n")
                print_json_box(data, "SIM DATABASE RESPONSE")
    
    # Final sparkle effect
    for _ in range(5):
        sparkles = ["✨", "🌟", "⭐", "💫", "🔸", "🔹"]
        sparkle = random.choice(sparkles)
        print(f"\r{Colors.YELLOW}{' ' * 20}{sparkle}{' ' * 20}{Colors.END}", end='\r')
        time.sleep(0.1)
    
    print()

def get_fancy_input():
    """Enhanced input with animation"""
    input_frames = ["▹", "▸", "▻", "▶", "▷", "►"]
    for i in range(10):
        frame = input_frames[i % len(input_frames)]
        sys.stdout.write(f"\r{Colors.MAGENTA}{frame} Enter SIM Number: {Colors.GREEN}")
        sys.stdout.flush()
        time.sleep(0.1)
    
    user_input = input(f"{Colors.GREEN}")
    print(Colors.END, end='')
    return user_input.strip()

def main():
    # Display epic animated banner
    display_epic_banner()
    
    while True:
        print(f"\n{Colors.YELLOW}{'═' * 50}{Colors.END}")
        print(f"{Colors.CYAN}📱 Instructions:{Colors.END}")
        print(f"{Colors.GREEN}• Enter Pakistani SIM number (e.g., 3001234567)")
        print(f"• 'q' to quit | 'b' for banner | 'c' to clear")
        print(f"• 'm' for matrix effect | 'help' for commands{Colors.END}")
        print(f"{Colors.YELLOW}{'═' * 50}{Colors.END}")
        
        user_input = get_fancy_input()
        
        if user_input.lower() == 'q':
            # Exit animation
            goodbye_frames = ["👋", "🚪", "👋", "🚶", "🏃", "✈️"]
            for frame in goodbye_frames:
                os.system('clear' if os.name == 'posix' else 'cls')
                print(f"\n\n{Colors.YELLOW}{' ' * 20}{frame} Thank you! Goodbye! {frame}{' ' * 20}{Colors.END}\n")
                time.sleep(0.2)
            break
        elif user_input.lower() == 'b':
            display_epic_banner()
            continue
        elif user_input.lower() == 'c':
            os.system('clear' if os.name == 'posix' else 'cls')
            continue
        elif user_input.lower() == 'm':
            matrix_rain()
            continue
        elif user_input.lower() == 'help':
            print(f"\n{Colors.CYAN}Available Commands:{Colors.END}")
            commands = [
                ("q", "Quit the program"),
                ("b", "Show epic banner"),
                ("c", "Clear screen"),
                ("m", "Matrix rain effect"),
                ("help", "Show this help"),
                ("json", "View raw JSON response")
            ]
            for cmd, desc in commands:
                print(f"  {Colors.GREEN}{cmd:10}{Colors.END} {desc}")
            continue
        elif not user_input:
            print(f"{Colors.RED}⚠️ Please enter a SIM number{Colors.END}")
            continue
        
        # Validate input
        if not user_input.isdigit() or len(user_input) < 10:
            print(f"{Colors.RED}❌ Invalid format! Use digits only without 0 (e.g., 3001234567){Colors.END}")
            continue
        
        # Show epic loading animation
        epic_loading_animation(f"QUERYING {user_input}")
        
        # Query API
        result, raw_json = lookup_sim(user_input)
        
        # Display animated results
        display_animated_result(result, raw_json, user_input)
        
        # Continue prompt with animation
        continue_frames = ["⏎", "↩️", "↵", "⤶"]
        for i in range(15):
            frame = continue_frames[i % len(continue_frames)]
            sys.stdout.write(f"\r{Colors.YELLOW}{frame} Press Enter to continue or 'q' to quit...{Colors.END}")
            sys.stdout.flush()
            time.sleep(0.1)
        
        response = input(f"\r{Colors.YELLOW}⏎ Press Enter to continue or 'q' to quit... {Colors.END}").strip().lower()
        if response == 'q':
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}⚠️ Program interrupted by user{Colors.END}")
        print(f"{Colors.YELLOW}👋 Goodbye!{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}💥 An unexpected error occurred: {str(e)}{Colors.END}")

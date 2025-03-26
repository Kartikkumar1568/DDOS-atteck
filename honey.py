import random
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

messages = [
    "You have been hacked!",
    "System breach detected!",
    "Access granted to root...",
    "All your base are belong to us!",
    "Initiating data exfiltration...",
    "Virus uploaded successfully!",
    "Critical security flaw exploited!"
]

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
styles = [Style.BRIGHT, Style.NORMAL, Style.DIM]

while True:
    msg = random.choice(messages)
    color = random.choice(colors)
    style = random.choice(styles)
    print(style + color + msg, flush=True)

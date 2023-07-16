import os
import sys
import signal
import hashlib
import time

from datetime import datetime
from colorama import Fore

from driver import Alterzone

def handler(signum, frame):
    print(f"{Fore.WHITE}└───[{Fore.GREEN}ALTERZONE AIO{Fore.WHITE}]")
    sys.exit()

def main():
    signal.signal(signal.SIGINT, handler)
    os.system("") # weird colorama bug??
    print(f"{Fore.WHITE}┌───[{Fore.GREEN}ALTERZONE AIO{Fore.WHITE}] Inicjalizacja...")
    alterzone_link = 'https://alterzone.pl/rejestracja'
    limited_offer = False

    now = datetime.now().strftime("%H:%M:%S")
    user_input = input(f"{Fore.WHITE}│ [{Fore.GREEN}ALTERZONE AIO{Fore.WHITE}] [{Fore.GREEN}{now}{Fore.WHITE}] {Fore.GREEN}Czy chcesz uzyc ref-linka do rejestracji? (tak/nie): {Fore.WHITE}")
    if user_input.lower() == 'tak':
        now = datetime.now().strftime("%H:%M:%S")
        user_input = input(f"{Fore.WHITE}│ [{Fore.GREEN}ALTERZONE AIO{Fore.WHITE}] [{Fore.GREEN}{now}{Fore.WHITE}] {Fore.GREEN}Podaj link: {Fore.WHITE}")
        if 'https://alterzone.pl/R/' in user_input:
            alterzone_link = user_input
        else:
            print(f"{Fore.WHITE}└───[{Fore.GREEN}ALTERZONE AIO{Fore.WHITE}] Niewlasciwy ref-link!")
            time.sleep(3)
            sys.exit()
    elif user_input.lower() == 'nie':
        pass
    else:
        print(f"{Fore.WHITE}└───[{Fore.GREEN}ALTERZONE AIO{Fore.WHITE}] Niewlasciwa opcja!")
        time.sleep(3)
        sys.exit()
    
    now = datetime.now().strftime("%H:%M:%S")
    user_input = input(f"{Fore.WHITE}│ [{Fore.GREEN}ALTERZONE AIO{Fore.WHITE}] [{Fore.GREEN}{now}{Fore.WHITE}] {Fore.GREEN}Czy chcesz skorzystac z oferty limitowanej? (tak/nie): {Fore.WHITE}")
    if user_input.lower() == 'tak':
         limited_offer = True
    elif user_input.lower() == 'nie':
        pass
    else:
        print(f"{Fore.WHITE}└───[{Fore.GREEN}ALTERZONE AIO{Fore.WHITE}] Niewlasciwa opcja!")
        time.sleep(3)
        sys.exit()

    # init
    Alterzone(limited_offer).execute(alterzone_link)

if __name__ == "__main__":
     if os.name == "nt":
        main()
     else:
        print(f"{Fore.WHITE}│ [{Fore.GREEN}ALTERZONE AIO{Fore.WHITE}] {Fore.GREEN}Twoj system operacyjny nie jest wspierany!")
        time.sleep(3)
        sys.exit(0)
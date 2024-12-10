from config import *

def apresentacao():
    ascii_art = pyfiglet.figlet_format("QUESTOES")
    print(ascii_art)
    sleep(2)
    print(f"\033[95m 😎SEJA BEM VINDO AO BOT DE QUESTÕES. ESSE BOT FOI FEITO PELO VILHALVA (GITHUB -> @VILHALVA) \033[0m")
    sleep(2)

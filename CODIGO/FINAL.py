def final():
    from time import sleep
            
    print("=" *25, "\n  🌎CRÉDITOS:", "\n👤CRIADOR: SAMUEL MARTINS VILHALVA\n 🐱GITHUB: @VILHALVA \n📆DATA: 20/06/2022;\n👅LINGUAGEM: PYTHON\n", "=" *25)
    sleep(2)
    print("-" *20, "\n⛔FIM DO PROGRAMA!\n".center(10), "-" *20)    
    sleep(1)
    for c in range(30, 0, -1):
        print(f"⌛ESSE APP SERÁ FECHADO EM ({c}) SEGUNDOS!",end="\r")
        sleep(1)     
    sleep(1)
    exit()
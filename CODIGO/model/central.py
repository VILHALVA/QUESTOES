from config import *

def INICIO(materia): 
    global MATERIA
    MATERIA = materia   
    print(f"😃OLÁ NOVO USUÁRIO! IREI TE MANDAR ALGUMAS QUESTÕES DE: >>> {MATERIA} <<<.") 
    sleep(1)
    print("😃LEMBRANDO QUE VOCÊ SÓ IRÁ SER APROVADO COM MAIS DE 70% DE ACERTOS!") 
    sleep(1)
    print("😃ENTÃO VAMOS COMEÇAR!")
    for c in range(0, 101, 1):
        print(f"⌛CARREGANDO({c}%)...",end="\r")
        sleep(0.1) 
    print()

def VALOR_INT(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("😬ERRO! DIGITE UM VALOR INTEIRO!!!")
            continue
        except KeyboardInterrupt:
            print("🔺HOUVE ERRO! USUÁRIO NÃO DIGITOU VALOR!")
            return n
        else:
            return n 
    
def QUESTAO(msg):
    print()
    print("=" *20)
    print(msg)
    print("=" *20)
    
def RESPOSTA(CERTA, QUESTAO):
    global GABARITO
    if 'GABARITO' not in globals():
        GABARITO = [[],[]]  
        
    while True:
        RES = input("😎DIGITE SUA RESPOSTA:\n>>>").strip().upper()
        if not RES:
            print("⛔ERRO! VOCÊ DEVE DIGITAR UMA RESPOSTA.")
        elif RES not in "ABCD":
            print("⛔ERRO! RESPOSTA INVÁLIDA. DIGITE A, B, C OU D.")
        else:
            break

    if RES != CERTA:
        print(f"🤬VOCÊ ERROU! ALTERNATIVA CORRETA É '{CERTA}'")
        GABARITO[0].append(QUESTAO)
    else:
        print("😃CERTA RESPOSTA!")
        GABARITO[1].append(QUESTAO)
    sleep(1)

def FIM():
    TIME = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    TOTAL = len(GABARITO[1]) + len(GABARITO[0])
    ACERTOS = len(GABARITO[1])
    MEDIA = (ACERTOS / TOTAL) * 100

    RESULTADO = "👎REPROVADO" if ACERTOS < 0.7 * TOTAL else "👍APROVADO"

    RES = f'''
    =========================================
        🔴RESULTADO FINAL:   
    -----------------------------------------
    ⭐TIME: {TIME}
    ⭐MATERIA: {MATERIA}
    ⭐QUESTÕES CORRETAS: {GABARITO[1]}
    ⭐QUESTÕES ERRADAS: {GABARITO[0]}
    ⭐QUANTIDADE DE ACERTOS: {ACERTOS} QUESTÕES
    ⭐QUANTIDADE DE ERROS: {len(GABARITO[0])} QUESTÕES
    ⭐SUA MÉDIA FOI: {MEDIA:.0f}%
    ⭐RESULTADO: {RESULTADO}
    ------------------------------------------
    ==========================================
    '''
    
    print(RES)  
    sleep(3)

    salvar = input("😃VOCÊ DESEJA SALVAR ESSE RESULTADO FINAL? ENVIE 'S' PARA CONFIRMAR!:\n>>> ").strip().upper()

    if salvar == "S":
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
        files_dir = os.path.join(base_dir, 'files')

        if not os.path.exists(files_dir):
            os.makedirs(files_dir)

        TEMPO = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        file_name = f"QUESTOES_{MATERIA}_{TEMPO}.txt"
        file_path = os.path.join(files_dir, file_name)
        
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(RES)  
        print(f"😃O RESULTADO FINAL FOI SALVO COM SUCESSO EM '{file_path}'!")
        sleep(3)
    else:
        print("🤨TUDO BEM. O RESULTADO FINAL NÃO FOI SALVO!")
        sleep(3)

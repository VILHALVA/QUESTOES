from config import *
  
def INICIO(materia): 
    global MATERIA, RESPOSTAS_CORRETAS, RESPOSTAS_RESPONDIDAS
    MATERIA = materia
    RESPOSTAS_CORRETAS = {}
    RESPOSTAS_RESPONDIDAS = {}
    
    print(f"\033[93m 😃OLÁ NOVO USUÁRIO! IREI TE MANDAR ALGUMAS QUESTÕES DE: >>> {MATERIA} <<<. \033[0m") 
    sleep(1)
    print("\033[93m 😃LEMBRANDO QUE VOCÊ SÓ IRÁ SER APROVADO COM MAIS DE 70% DE ACERTOS! \033[0m") 
    sleep(1)
    print("\033[93m 😃ENTÃO VAMOS COMEÇAR!\033[0m")
    for c in range(0, 101, 1):
        print(f"\033[92m\033[4m ⌛CARREGANDO({c}%)... \033[0m", end="\r")
        sleep(0.1)
    print()

def VALOR_INT(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[91m 😬ERRO! DIGITE UM VALOR INTEIRO!!! \033[0m")
            continue
        except KeyboardInterrupt:
            print("\033[91m 🔺HOUVE ERRO! USUÁRIO NÃO DIGITOU VALOR! 033[0m")
            return n
        else:
            return n 

def QUESTAO(msg):
    print()
    print("=" * 20)
    print(msg)
    print("=" * 20)

def RESPOSTA(CERTA, QUESTAO):
    global GABARITO, RESPOSTAS_CORRETAS, RESPOSTAS_RESPONDIDAS
    if 'GABARITO' not in globals():
        GABARITO = [[],[]]  
    
    RESPOSTAS_CORRETAS[QUESTAO] = CERTA
    
    while True:
        RES = input("\033[93m 😎DIGITE SUA RESPOSTA:\n>>> \033[0m").strip().upper()
        if not RES:
            print("\033[91m ⛔ERRO! VOCÊ DEVE DIGITAR UMA RESPOSTA. \033[0m")
        elif RES not in "ABCD":
            print("\033[91m ⛔ERRO! RESPOSTA INVÁLIDA. DIGITE A, B, C OU D. \033[0m")
        else:
            break

    RESPOSTAS_RESPONDIDAS[QUESTAO] = RES

    if RES != CERTA:
        print(f"\033[91m 🤬VOCÊ ERROU! ALTERNATIVA CORRETA É '{CERTA}' \033[0m")
        GABARITO[0].append(QUESTAO)
    else:
        print("\033[92m 😃CERTA RESPOSTA! \033[0m")
        GABARITO[1].append(QUESTAO)
    sleep(1)

def FIM():
    TIME = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    TOTAL = len(GABARITO[1]) + len(GABARITO[0])
    ACERTOS = len(GABARITO[1])
    MEDIA = (ACERTOS / TOTAL) * 100
    SITUACAO = "👎REPROVADO" if ACERTOS < 0.7 * TOTAL else "👍APROVADO"

    RESULTADO = f'''
    =========================================
        🔴RESULTADO FINAL:   
    -----------------------------------------
    ⭐DATA E HORA: {TIME}
    ⭐MATÉRIA: {MATERIA}
    ⭐RESPOSTAS CORRETAS: {RESPOSTAS_CORRETAS}
    ⭐RESPOSTAS RESPONDIDAS: {RESPOSTAS_RESPONDIDAS}
    ⭐QUESTÕES QUE VOCÊ ACERTOU: {GABARITO[1]}
    ⭐QUESTÕES QUE VOCÊ ERROU: {GABARITO[0]}
    ⭐VOCÊ ACERTOU {ACERTOS} QUESTÕES
    ⭐VOCÊ ERROU {len(GABARITO[0])} QUESTÕES
    ⭐SUA MÉDIA FOI: {MEDIA:.0f}%
    ⭐SITUAÇÃO: {SITUACAO}
    -----------------------------------------
    =========================================
    '''

    print(RESULTADO)  
    sleep(3)

    salvar = input("\033[94m 😃VOCÊ DESEJA SALVAR ESSE RESULTADO FINAL? ENVIE 'S' PARA CONFIRMAR!:\n>>> \033[0m").strip().upper()

    if salvar == "S":
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
        files_dir = os.path.join(base_dir, 'files')

        if not os.path.exists(files_dir):
            os.makedirs(files_dir)

        TEMPO = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        file_name = f"QUESTOES_{MATERIA}_{TEMPO}.txt"
        file_path = os.path.join(files_dir, file_name)
        
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(RESULTADO)  
        print(f"\033[92m 😃O RESULTADO FINAL FOI SALVO COM SUCESSO EM '{file_path}'! \033[0m")
        sleep(3)
    else:
        print("\033[91m 🤨TUDO BEM. O RESULTADO FINAL NÃO FOI SALVO! \033[0m")
        sleep(3)

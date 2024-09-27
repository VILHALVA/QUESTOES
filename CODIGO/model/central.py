from config import *

def INICIO(MATERIA):
    print(f"😃OLÁ NOVO JOGADOR! IREI TE MANDAR ALGUMAS QUESTÕES DE: >>> {MATERIA} <<<.") 
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
    print("=" *100)
    print(msg)
    print("=" *100)
    
GABARITO = [[],[]]
def RESPOSTA(CERTA, QUESTAO):
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
    TOTAL = len(GABARITO[1]) + len(GABARITO[0])
    ACERTOS = len(GABARITO[1])
    MEDIA = (ACERTOS / TOTAL) * 100

    if ACERTOS < 0.7 * TOTAL:
        RESULTADO = "👎REPROVADO"
    else:
        RESULTADO = "👍APROVADO"

    print("=" * 20)
    print("       RESULTADO FINAL            ")
    print("_" * 20)
    print(f"⭐QUESTÕES CORRETAS: {GABARITO[1]}")
    print(f"⭐QUESTÕES ERRADAS: {GABARITO[0]}")
    print(f"⭐QUANTIDADE DE ACERTOS: {ACERTOS} QUESTÕES")
    print(f"⭐QUANTIDADE DE ERROS: {len(GABARITO[0])} QUESTÕES")
    print(f"⭐SUA MÉDIA FOI: {MEDIA:.0f}%")
    print(f"⭐RESULTADO: {RESULTADO}")
    print("_" * 20)
    print("=" * 20)
    sleep(3)
    

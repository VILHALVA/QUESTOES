from config import *

def INICIO(MATERIA):
    print(f"😃Olá novo jogador! Irei te mandar algumas questões de: >>> {MATERIA} <<<.") 
    sleep(1)
    print("😃Lembrando que você só irá ser aprovado com mais de 70% de acertos!") 
    sleep(1)
    print("😃Então vamos começar!")
    for c in range(0, 101, 1):
        print(f"⌛CARREGANDO({c}%)...",end="\r")
        sleep(0.1) 
    print()

def VALOR_INT(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("😬ERRO! Digite um valor Inteiro!!!")
            continue
        except KeyboardInterrupt:
            print("🔺Houve erro! Usuário não digitou valor!")
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
        RES = input("😎Digite sua resposta:\n>>>").strip().upper()
        if not RES:
            print("⛔ERRO! Você deve digitar uma resposta.")
        elif RES not in "ABCD":
            print("⛔ERRO! Resposta inválida. Digite A, B, C ou D.")
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

    print("=" * 100)
    print("       RESULTADO FINAL            ")
    print("_" * 100)
    print(f"⭐QUESTÕES CORRETAS: {GABARITO[1]}")
    print(f"⭐QUESTÕES ERRADAS: {GABARITO[0]}")
    print(f"⭐QUANTIDADE DE ACERTOS: {ACERTOS} QUESTÕES")
    print(f"⭐QUANTIDADE DE ERROS: {len(GABARITO[0])} QUESTÕES")
    print(f"⭐SUA MÉDIA FOI: {MEDIA:.0f}%")
    print(f"⭐RESULTADO: {RESULTADO}")
    print("_" * 100)
    print("=" * 100)
    sleep(3)
    
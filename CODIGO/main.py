from config import *

def main():
    apresentacao()  
    opcoes = {
        0: final,
        1: portugues,
        2: matematica,
        3: fisica,
        4: quimica,
        5: biologia,
        6: historia,
        7: geografia,
        8: filosofia,
        9: sociologia,
        10: artes,
        11: religiao,
        12: literatura,
        13: tecnologia,
        14: medicina,
        15: direitos,
        16: politica,
        17: economia,
        18: marketing,
        19: teologia_ibadep,
        20: teologia_qi,
        21: historia_do_brasil,
        22: geografia_do_brasil,
        23: civismo,
        24: informatica,
        25: engenharia_civil,
        26: agronomia,
        27: turismo,
        28: engenharia_eletrica,
        29: administracao,
        30: pedagogia,
        31: psicanalise,
        32: jornalismo,
        33: enfermagem,
        34: nutricao,
        35: educacao_fisica,
        36: espanhol,
        37: ingles,
        38: hebraico,
        39: grego,
        40: biomedicina,
        41: veterinaria,
        42: advocacia,
        43: fisioterapia,
        44: ciberseguranca,
        45: engenharia_mecanica,
        46: antropologia,
        47: geologia,
        48: paleontologia,
        49: aviacao,
        50: engenharia_florestal
    } 
    
    while True:
        print('''\033[91m\033[1m
            MENU PRINCIPAL:
            [ 0 ] SAIR DO PROGRAMA
            [ 1 ] PORTUGUES
            [ 2 ] MATEMATICA
            [ 3 ] FISICA
            [ 4 ] QUIMICA
            [ 5 ] BIOLOGIA
            [ 6 ] HISTORIA
            [ 7 ] GEOGRAFIA
            [ 8 ] FILOSOFIA
            [ 9 ] SOCIOLOGIA
            [ 10 ] ARTES
            [ 11 ] RELIGIAO
            [ 12 ] LITERATURA
            [ 13 ] TECNOLOGIA
            [ 14 ] MEDICINA
            [ 15 ] DIREITOS
            [ 16 ] POLITICA
            [ 17 ] ECONOMIA
            [ 18 ] MARKETING
            [ 19 ] TEOLOGIA IBADEP
            [ 20 ] TEOLOGIA QI
            [ 21 ] HISTÓRIA DO BRASIL
            [ 22 ] GEOGRAFIA DO BRASIL
            [ 23 ] CIVISMO
            [ 24 ] INFORMATICA
            [ 25 ] ENGENHARIA CIVIL
            [ 26 ] AGRONOMIA
            [ 27 ] TURISMO
            [ 28 ] ENGENHARIA ELÉTRICA
            [ 29 ] ADMINISTRAÇÃO EMPRESARIAL
            [ 30 ] PEDAGOGIA
            [ 31 ] PSICANÁLISE
            [ 32 ] JORNALISMO
            [ 33 ] ENFERMAGEM
            [ 34 ] NUTRIÇÃO
            [ 35 ] EDUCAÇÃO FÍSICA
            [ 36 ] ESPANHOL
            [ 37 ] INGLÊS
            [ 38 ] HEBRAICO
            [ 39 ] GREGO
            [ 40 ] BIOMEDICINA
            [ 41 ] MEDICINA VETERINARIA
            [ 42 ] ADVOCACIA
            [ 43 ] FISIOTERAPIA
            [ 44 ] CIBER SEGURANÇA
            [ 45 ] ENGENHARIA MECÂNICA
            [ 46 ] ANTROPOLOGIA
            [ 47 ] GEOLOGIA
            [ 48 ] PALEONTOLOGIA
            [ 49 ] AVIAÇÃO
            [ 50 ] ENGENHARIA FLORESTAL
            \033[0m
            ''')
        sleep(1)
        opcao = VALOR_INT("\033[93m 😎ESCOLHA UMA MATÉRIA:\n>>> \033[0m")       
        if opcao in opcoes:
            opcoes[opcao]()  
        else:
            print("\033[91m 😠OPÇÃO INVÁLIDA. TENTE NOVAMENTE! \033[0m")

if __name__ == "__main__":
    main()

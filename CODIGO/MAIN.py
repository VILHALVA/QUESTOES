from time import sleep
from APRESENTACAO import apresentacao
from AAAA import VALOR_INT
from FINAL import final

from PORTUGUES import portugues
from MATEMATICA import matematica
from FISICA import fisica
from QUIMICA import quimica
from BIOLOGIA import biologia
from HISTORIA import historia
from GEOGRAFIA import geografia
from FILOSOFIA import filosofia
from SOCIOLOGIA import sociologia
from ARTES import artes
from RELIGIAO import religiao
from LITERATURA import literatura
from TECNOLOGIA import tecnologia
from MEDICINA import medicina
from DIREITOS import direitos
from POLITICA import politica
from ECONOMIA import economia
from MARKETING import marketing
from TEOLOGIA_IBADEP import teologia_ibadep
from TEOLOGIA_QI import teologia_qi
from HISTORIA_DO_BRASIL import historia_do_brasil
from GEOGRAFIA_DO_BRASIL import geografia_do_brasil
from CIVISMO import civismo
from INFORMATICA import informatica
from ENGENHARIA_CIVIL import engenharia_civil
from AGRONOMIA import agronomia
from TURISMO import turismo
from ENGENHARIA_ELETRICA import engenharia_eletrica
from ADMINISTRACAO import administracao
from PEDAGOGIA import pedagogia
from PSICANALISE import psicanalise
from JORNALISMO import jornalismo
from ENFERMAGEM import enfermagem
from NUTRICAO import nutricao
from EDUCACAO_FISICA import educacao_fisica
from ESPANHOL import espanhol
from INGLES import ingles
from HEBRAICO import hebraico
from GREGO import grego
from BIOMEDICINA import biomedicina
from VETERINARIA import veterinaria
from ADVOCACIA import advocacia
from FISIOTERAPIA import fisioterapia
from CIBERSEGURANCA import ciberseguranca
from ENGENHARIA_MECANICA import engenharia_mecanica
from ANTROPOLOGIA import antropologia
from GEOLOGIA import geologia
from PALEONTOLOGIA import paleontologia
from AVIACAO import aviacao
from ENGENHARIA_FLORESTAL import engenharia_florestal

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
        print('''
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
            ''')
        sleep(1)
        opcao = VALOR_INT("😎ESCOLHA UMA MATÉRIA:\n>>>")       
        if opcao in opcoes:
            opcoes[opcao]()  
        else:
            print("😠Opção inválida. Tente novamente!")

if __name__ == "__main__":
    main()

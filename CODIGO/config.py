from time import sleep

from model.central import (
    INICIO, 
    VALOR_INT, 
    QUESTAO,
    RESPOSTA, 
    FIM
)

from model.apresentacao import apresentacao
from model.final import final
from plugins.portugues import portugues
from plugins.matematica import matematica
from plugins.fisica import fisica
from plugins.quimica import quimica
from plugins.biologia import biologia
from plugins.historia import historia
from plugins.geografia import geografia
from plugins.filosofia import filosofia
from plugins.sociologia import sociologia
from plugins.artes import artes
from plugins.religiao import religiao
from plugins.literatura import literatura
from plugins.tecnologia import tecnologia
from plugins.medicina import medicina
from plugins.direitos import direitos
from plugins.politica import politica
from plugins.economia import economia
from plugins.marketing import marketing
from plugins.teologia_ibadep import teologia_ibadep
from plugins.teologia_qi import teologia_qi
from plugins.historia_do_brasil import historia_do_brasil
from plugins.geografia_do_brasil import geografia_do_brasil
from plugins.civismo import civismo
from plugins.informatica import informatica
from plugins.engenharia_civil import engenharia_civil
from plugins.agronomia import agronomia
from plugins.turismo import turismo
from plugins.engenharia_eletrica import engenharia_eletrica
from plugins.administracao import administracao
from plugins.pedagogia import pedagogia
from plugins.psicanalise import psicanalise
from plugins.jornalismo import jornalismo
from plugins.enfermagem import enfermagem
from plugins.nutricao import nutricao
from plugins.educacao_fisica import educacao_fisica
from plugins.espanhol import espanhol
from plugins.ingles import ingles
from plugins.hebraico import hebraico
from plugins.grego import grego
from plugins.biomedicina import biomedicina
from plugins.veterinaria import veterinaria
from plugins.advocacia import advocacia
from plugins.fisioterapia import fisioterapia
from plugins.ciberseguranca import ciberseguranca
from plugins.engenharia_mecanica import engenharia_mecanica
from plugins.antropologia import antropologia
from plugins.geologia import geologia
from plugins.paleontologia import paleontologia
from plugins.aviacao import aviacao
from plugins.engenharia_florestal import engenharia_florestal

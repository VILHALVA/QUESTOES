from config import *

def engenharia_eletrica():
    INICIO("ENGENHARIA ELÉTRICA")

    QUESTAO('''01) O que é um circuito elétrico trifásico e como ele se diferencia de um circuito monofásico?
        A) Circuito com três dispositivos conectados em série, diferente do circuito monofásico que possui apenas um dispositivo.
        B) Sistema de distribuição de energia elétrica com três fases, cada uma defasada em 120 graus, ao contrário do monofásico que possui apenas uma fase.
        C) Circuito que opera com três correntes elétricas independentes, enquanto o monofásico opera com apenas uma corrente.
        D) Circuito que utiliza três tipos diferentes de componentes elétricos.
    ''')
    RESPOSTA(CERTA="B", QUESTAO=1)

    QUESTAO('''02) O que é um transformador e qual é a sua função em sistemas de distribuição de energia elétrica?
        A) Dispositivo que converte corrente contínua em corrente alternada.
        B) Equipamento utilizado para armazenar energia elétrica.
        C) Dispositivo que modifica a tensão de um circuito elétrico, permitindo sua transmissão eficiente.
        D) Componente que regula a intensidade da corrente elétrica em um circuito.
    ''')
    RESPOSTA(CERTA="C", QUESTAO=2)

    QUESTAO('''03) O que é um diodo semicondutor e como ele é utilizado em eletrônica?
        A) Componente que permite a passagem de corrente elétrica em apenas uma direção, utilizado em retificadores.
        B) Componente que amplifica sinais de áudio.
        C) Dispositivo utilizado para armazenar carga elétrica.
        D) Componente que regula a intensidade da corrente em um circuito.
    ''')
    RESPOSTA(CERTA="A", QUESTAO=3)

    QUESTAO('''04) Qual é a diferença entre corrente alternada (CA) e corrente contínua (CC)?
        A) Corrente alternada é unidirecional, enquanto corrente contínua muda de direção periodicamente.
        B) Corrente contínua é utilizada apenas em residências, enquanto corrente alternada é utilizada em indústrias.
        C) Corrente alternada é utilizada em dispositivos eletrônicos, enquanto corrente contínua é utilizada em motores elétricos.
        D) Corrente contínua é gerada por fontes renováveis, enquanto corrente alternada é gerada por fontes não renováveis.
    ''')
    RESPOSTA(CERTA="A", QUESTAO=4)

    QUESTAO('''05) O que é um motor de indução trifásico e onde ele é comumente utilizado?
        A) Motor elétrico que funciona apenas com uma fase, utilizado em dispositivos de baixo consumo.
        B) Motor elétrico que opera com três fases, comum em sistemas industriais e motores de máquinas.
        C) Motor que utiliza indução magnética, utilizado apenas em aparelhos domésticos.
        D) Motor elétrico que opera exclusivamente com corrente contínua.
    ''')
    RESPOSTA(CERTA="B", QUESTAO=5)

    QUESTAO('''06) O que é um circuito integrado e como ele revolucionou a eletrônica?
        A) Componente que permite a passagem de corrente em uma única direção.
        B) Dispositivo utilizado para armazenar dados em computadores.
        C) Conjunto de componentes eletrônicos interconectados em um único chip, possibilitando a miniaturização de dispositivos eletrônicos.
        D) Equipamento que gera sinais de áudio.
    ''')
    RESPOSTA(CERTA="C", QUESTAO=6)

    QUESTAO('''07) O que é um sistema de controle PID (Proporcional, Integral, Derivativo) e onde ele é aplicado na engenharia elétrica?
        A) Sistema de controle utilizado em motores de indução.
        B) Sistema de controle que utiliza apenas a parte integral para correção de erros.
        C) Sistema de controle utilizado em circuitos de iluminação.
        D) Sistema de controle que combina proporção, integral e derivativo para regular processos dinâmicos.
    ''')
    RESPOSTA(CERTA="D", QUESTAO=7)

    QUESTAO('''08) O que é a lei de Ohm e como ela relaciona tensão, corrente e resistência em um circuito elétrico?
        A) V = R * I, onde V é a tensão, R é a resistência e I é a corrente.
        B) P = V * I, onde P é a potência, V é a tensão e I é a corrente.
        C) I = V / R, onde I é a corrente, V é a tensão e R é a resistência.
        D) R = P / I^2, onde R é a resistência, P é a potência e I é a corrente.
    ''')
    RESPOSTA(CERTA="C", QUESTAO=8)

    QUESTAO('''09) O que é um relé e como ele é utilizado em sistemas de controle elétrico?
        A) Componente que transforma corrente alternada em corrente contínua.
        B) Dispositivo que regula a intensidade da corrente em um circuito.
        C) Interruptor controlado por uma corrente em outro circuito, utilizado para controlar cargas elétricas.
        D) Sensor de temperatura utilizado em sistemas de refrigeração.
    ''')
    RESPOSTA(CERTA="C", QUESTAO=9)

    QUESTAO('''10) O que é a potência aparente em um circuito elétrico e como ela difere da potência ativa?
        A) Potência aparente é a soma vetorial da potência ativa e reativa, enquanto a potência ativa é a componente real.
        B) Potência aparente é a potência máxima que um dispositivo pode fornecer, enquanto a potência ativa é a efetivamente consumida.
        C) Potência aparente é a potência média ao longo do tempo, enquanto a potência ativa é instantânea.
        D) Potência aparente e potência ativa são conceitos equivalentes em circuitos elétricos.
    ''')
    RESPOSTA(CERTA="A", QUESTAO=10)

    FIM()

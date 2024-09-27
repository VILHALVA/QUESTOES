from config import *

def nutricao():
    INICIO("NUTRIÇÃO")

    QUESTAO('''01) Explique a diferença entre macronutrientes e micronutrientes e forneça exemplos de cada um.
        A) Macronutrientes são nutrientes essenciais em quantidades mínimas, enquanto micronutrientes são necessários em grandes quantidades. Exemplos: carboidratos, proteínas e gorduras (macronutrientes); vitaminas e minerais (micronutrientes).
        B) Macronutrientes são nutrientes essenciais em grandes quantidades, enquanto micronutrientes são necessários em quantidades mínimas. Exemplos: vitaminas e minerais (macronutrientes); carboidratos, proteínas e gorduras (micronutrientes).
        C) Ambos os termos se referem a nutrientes que devem ser consumidos em quantidades mínimas. Exemplos: água, fibras e antioxidantes.
        D) Não há diferença significativa entre macronutrientes e micronutrientes.
    ''')
    RESPOSTA(CERTA="A", QUESTAO=1)

    QUESTAO('''02) O que é o índice glicêmico (IG) e como ele influencia as escolhas alimentares para controle da glicemia?
        A) Medida do teor calórico dos alimentos.
        B) Classificação dos alimentos com base na quantidade de vitaminas e minerais.
        C) Indicador da velocidade com que um alimento eleva os níveis de glicose no sangue. Alimentos com IG baixo são absorvidos lentamente, enquanto os de IG alto são absorvidos rapidamente.
        D) Avaliação do teor de proteínas dos alimentos.
    ''')
    RESPOSTA(CERTA="C", QUESTAO=2)

    QUESTAO('''03) Explique a importância dos antioxidantes na alimentação e forneça exemplos de alimentos ricos nesses compostos.
        A) Antioxidantes são substâncias que devem ser evitadas na alimentação para prevenir o envelhecimento precoce.
        B) São compostos que promovem a oxidação das células, acelerando o envelhecimento. Exemplos: frutas e vegetais coloridos.
        C) Substâncias que combatem os radicais livres, protegendo as células do estresse oxidativo. Exemplos: vitamina C, vitamina E, betacaroteno (encontrados em frutas, vegetais e nozes).
        D) Não há evidências científicas sobre os benefícios dos antioxidantes na alimentação.
    ''')
    RESPOSTA(CERTA="C", QUESTAO=3)

    QUESTAO('''04) O que é a recomendação diária de fibras alimentares e qual é o papel dessas fibras na saúde digestiva?
        A) Recomendação de no mínimo 5 gramas de fibras por dia. Elas promovem a constipação e dificultam a digestão.
        B) Recomendação de 30 a 38 gramas de fibras por dia. Elas contribuem para a regularidade intestinal, redução do risco de doenças cardíacas e controle do peso.
        C) Não há recomendações específicas para o consumo de fibras. Elas têm papel secundário na saúde digestiva.
        D) Recomendação de 15 gramas de fibras por dia, especialmente provenientes de alimentos processados.
    ''')
    RESPOSTA(CERTA="B", QUESTAO=4)

    QUESTAO('''05) Explique o conceito de valor nutricional e como ele é apresentado nos rótulos alimentares.
        A) Valor nutricional refere-se à quantidade de calorias em um alimento, apresentada nos rótulos como a porcentagem de calorias diárias recomendadas.
        B) Indicador da quantidade de vitaminas e minerais essenciais em um alimento. Apresentado como uma lista de ingredientes.
        C) Conjunto de informações sobre os nutrientes presentes em um alimento e suas quantidades em porções específicas. Apresentado em uma tabela de informações nutricionais.
        D) Avaliação subjetiva da qualidade nutricional de um alimento, sem dados específicos.
    ''')
    RESPOSTA(CERTA="C", QUESTAO=5)

    QUESTAO('''06) O que é a dieta mediterrânea e quais são os benefícios associados a esse padrão alimentar?
        A) Dieta baseada em produtos industrializados e fast food.
        B) Padrão alimentar caracterizado pelo consumo de frutas, vegetais, azeite de oliva, peixe, nozes e sementes. Associada a benefícios para a saúde cardiovascular e redução do risco de doenças crônicas.
        C) Dieta vegetariana com foco exclusivo em proteínas vegetais.
        D) Dieta rica em carnes vermelhas e gorduras saturadas.
    ''')
    RESPOSTA(CERTA="B", QUESTAO=6)

    QUESTAO('''07) Explique o papel dos ácidos graxos ômega-3 na alimentação e forneça fontes alimentares desses nutrientes.
        A) Ácidos graxos ômega-3 são prejudiciais à saúde cardiovascular e devem ser evitados.
        B) Contribuem para a saúde do sistema nervoso e cardiovascular. Fontes: peixes de água fria (salmão, sardinha), linhaça, chia e nozes.
        C) Não desempenham papel significativo na saúde humana.
        D) São encontrados apenas em suplementos alimentares, não em alimentos naturais.
    ''')
    RESPOSTA(CERTA="B", QUESTAO=7)

    QUESTAO('''08) O que é a intolerância à lactose e como ela afeta a digestão de produtos lácteos?
        A) Inabilidade do organismo em digerir qualquer quantidade de lactose, causando desconforto gastrointestinal severo.
        B) Condição que permite o consumo ilimitado de produtos lácteos sem efeitos colaterais.
        C) Dificuldade na digestão da lactose devido à falta da enzima lactase. Pode resultar em sintomas como gases, inchaço e diarreia.
        D) Intolerância à lactose é uma condição rara e não afeta a maioria da população.
    ''')
    RESPOSTA(CERTA="C", QUESTAO=8)

    QUESTAO('''09) Explique a importância do ferro na alimentação e como a deficiência desse mineral pode impactar a saúde.
        A) Ferro é um mineral dispensável na alimentação.
        B) Importante para a formação de ossos e dentes. Deficiência pode levar à osteoporose.
        C) Nutriente essencial para a formação de hemoglobina, transporte de oxigênio no sangue. A deficiência pode causar anemia.
        D) Não há impacto significativo da deficiência de ferro na saúde.
    ''')
    RESPOSTA(CERTA="C", QUESTAO=9)

    QUESTAO('''10) O que é a pirâmide alimentar e como ela pode ser utilizada como guia para uma alimentação saudável?
        A) Modelo que sugere o consumo prioritário de alimentos processados e industrializados.
        B) Representação gráfica que indica a importância de uma dieta baseada em proteínas animais.
        C) Guia visual que mostra a proporção adequada de diferentes grupos alimentares para uma alimentação equilibrada, como cereais, frutas, vegetais, proteínas e gorduras.
        D) Ferramenta exclusiva para dietas de emagrecimento.
    ''')
    RESPOSTA(CERTA="C", QUESTAO=10)

    FIM()

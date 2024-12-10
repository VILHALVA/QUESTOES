# QUESTOES
👨‍💻QUESTÕES É UM BOT DE SIMULADOR DE ENEM QUE RODA NO CONSOLE DA IDE.

<img src="./IMAGENS/FOTO_01.png" align="center" width="500"> <br>
<img src="./IMAGENS/FOTO_02.png" align="center" width="500"> <br>
<img src="./IMAGENS/FOTO_03.png" align="center" width="500"> <br>

## DESCRIÇÃO:
O Bot é um quiz interativo que apresenta perguntas sobre uma matéria específica. A seguir, uma descrição resumida de suas funcionalidades:

1. **Menu Principal:** O usuário pode escolher entre mais de 50 matérias disponíveis.

2. **Boas-Vindas:** O bot saúda o jogador e informa sobre a matéria em questão.

3. **Perguntas:** O usuário recebe uma série de perguntas relacionadas à matéria selecionada.

4. **Respostas:** O bot aceita respostas (A, B, C ou D) para cada pergunta.

5. **Feedback:** Fornece retorno imediato sobre a correção das respostas.

6. **Resultado Final:** Ao término do quiz, são exibidas estatísticas que incluem o nome da matéria, a data e a hora, respostas corretas, respostas respondidas, questões que você acertou, questões que você errou, quantidade de acertos, quantidade de erros, média de acertos, e a aprovação ou reprovação do jogador com base em uma porcentagem mínima de acertos.

7. **Salvar Resultado Final:** O sistema perguntará se o usuário deseja salvar as informações. Se afirmativo, o resultado será salvo em um arquivo `.txt` no diretório `./CODIGO/files`, com o nome `QUESTOES_{MATERIA}_{TIME}.txt`, contendo os mesmos dados exibidos no console.

## O QUE É O RESULTADO FINAL?
O **"RESULTADO FINAL"** é uma **compilação dos dados gerados ao longo de uma simulação de perguntas e respostas**, destinada a fornecer uma visão geral do desempenho do usuário. Ele é apresentado em um formato bem estruturado e organizado, com as seguintes informações:

### SUA ESTRUTURA:
1. **DATA E HORA**:
   - Indica o momento exato em que o resultado foi gerado, com formato `DD/MM/AAAA HH:MM:SS`.

2. **MATÉRIA**:
   - Identifica o tema ou disciplina das questões respondidas.

3. **RESPOSTAS CORRETAS**:
   - Um dicionário que mostra quais eram as respostas certas para cada pergunta.  
   Exemplo: `{1: 'D', 2: 'B', ...}` (onde o número da questão é associado à resposta correta).

4. **RESPOSTAS RESPONDIDAS**:
   - Um dicionário que exibe as respostas fornecidas pelo usuário para cada pergunta.  
   Exemplo: `{1: 'D', 2: 'A', ...}`.

5. **QUESTÕES QUE VOCÊ ACERTOU**:
   - Lista de números das questões respondidas corretamente pelo usuário.  
   Exemplo: `[1, 2, 4, 5]`.

6. **QUESTÕES QUE VOCÊ ERROU**:
   - Lista de números das questões que o usuário errou.  
   Exemplo: `[3, 6, 7]`.

7. **VOCÊ ACERTOU**:
   - A quantidade total de questões respondidas corretamente.  
   Exemplo: `7 QUESTÕES`.

8. **VOCÊ ERROU**:
   - A quantidade total de questões respondidas incorretamente.  
   Exemplo: `3 QUESTÕES`.

9. **SUA MÉDIA FOI**:
   - Percentual de acertos em relação ao total de questões respondidas. Calculado como:
     \[
     \text{Média (\%)} = \left( \frac{\text{Número de acertos}}{\text{Total de questões}} \right) \times 100
     \]
   Exemplo: `70%`.

10. **SITUAÇÃO**:
    - Determina se o usuário foi aprovado ou reprovado, baseado em um critério de acertos mínimo (70% no caso):
      - 👍 APROVADO (se a média for maior ou igual a 70%).
      - 👎 REPROVADO (se a média for inferior a 70%).

### PROPÓSITO:
- O **RESULTADO FINAL** serve como um relatório detalhado e objetivo para que o usuário possa:
   1. **Feedback Educacional**: Pode ser utilizado para práticas de estudo, simulando provas e avaliando o progresso.
   2. **Registro Histórico**: Ao salvar os resultados, o usuário pode acompanhar sua evolução ao longo do tempo.
   3. **Geração de Relatórios**: Facilita a criação de relatórios para análises ou compartilhamento de dados com professores ou colegas.

## EXECUTANDO O PROJETO:
1. **Instalar as dependências**:
   - Antes de rodar o bot, é essencial garantir que todas as dependências estejam instaladas. No terminal, navegue até o diretório `CODIGO` e execute o seguinte comando para instalar os pacotes listados no arquivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

2. **Execute o programa:**
   - Para iniciar o programa, execute o comando abaixo:
   ```bash
   python main.py
   ```

3. **Escolha da Matéria:**
   - Assim que o bot iniciar, você verá um menu principal no console com várias matérias numeradas.
   - Leia as matérias disponíveis e digite o número correspondente à matéria que deseja responder.

4. **Responda às perguntas:**
   - O bot executará a matéria que você selecionou.
   - Responda às perguntas corretamente, enviando apenas uma das opções: `A`, `B`, `C` ou `D`.
   - Após apresentar o `RESULTADO FINAL`, o bot perguntará se você deseja salvar as informações. Envie `S` para confirmar ou qualquer outro caractere para recusar.

5. **Retorno ao menu principal:**
   - Após a execução de cada materia, o bot retornará automaticamente ao menu principal, permitindo que você escolha outra materia ou opte por sair.

6. **Saindo do programa:**
   - Quando desejar encerrar o programa, digite `0` no menu principal. Isso encerrará o bot de forma segura.

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens e tecnologias, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS E MAIS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)
- [CLIQUE AQUI PARA VER O HISTÓRICO DE ATUALIZAÇÕES](./UPDATES.md)

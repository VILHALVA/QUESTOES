# ATUALIZAÇÕES:
## VERSÃO 1.7 - 26/09/2024:
### ✅ PRINCIPAIS MUDANÇAS REALIZADAS NA ESTRUTURA DO PROJETO:
1. **Novo arquivo `config.py`**:
   - 🔸 Criado para centralizar todas as importações e dependências do projeto. Agora, todos os arquivos fazem referência a este arquivo, simplificando a gestão de imports e prevenindo possíveis conflitos de importação.

2. **Renomeação e reorganização de arquivos**:
   - 🔸 O antigo arquivo `AAAA.py` foi renomeado para `central.py` e movido para o diretório `model`.
   - 🔸 As funções `apresentação` e `final` agora estão localizadas nos arquivos `apresentacao.py` e `final.py`, dentro do diretório `model`.

3. **Padronização de nomes de arquivos**:
   - 🔸 Todos os arquivos foram renomeados, deixando de estar em UPPERCASE para ficarem em lowercase, seguindo boas práticas de nomeação.

4. **Reclassificação do projeto**:
   - ✅ Este projeto foi reclassificado e não faz mais parte da categoria de [APLICATIVOS](https://github.com/VILHALVA?tab=repositories&q=topic:APLICATIVO+topic:TERMINAL). Agora ele pertence à categoria de [BOTS](https://github.com/VILHALVA?tab=repositories&q=topic:BOT+topic:TERMINAL). Com isso, o executável e o instalador foram removidos.

### 🔵 ESTRUTURA DE DIRETÓRIOS:
- **Antes:**
  ```plaintext
  /CODIGO
  │
  ├── MAIN.py
  ├── AAAA.py
  └── APRESENTACAO.py
  └── // Outros arquivos...
  ```

- **Depois:**
  ```plaintext
  /CODIGO
  │
  ├── /plugins
  │   ├── matematica.py
  │   ├── biologia.py
  │   └── // Outros arquivos...
  │
  ├── /model
  │   └── central.py
  │   └── apresentacao.py
  |   └── final.py
  ├── config.py
  └── main.py
  ```

---

## VERSÃO 1.6 - 29/06/2024:
* ✅Foi criado um instalador para Windows X64 apartir do executavel.
---

## VERSÃO 1.5 - 18/01/2024:
* ✅No `MENU PRINCIPAL`, substituímos as estruturas condicionais (if, elif) por um dicionário para mapear as opções diretamente para as funções correspondentes.
* ✅Foi adicionado um laço de repetição: Toda a vez que o usuário terminar de responder as questões e sair o resultado, o programa reinicia automaticamente; Dando a oportunidade para responder outras máterias sem a necissidade de reiniciar o App. O programa só para quando o usuário digitar `0` (SAIR DO PROGRAMA). 
* ✅30 novas máterias foram adicionadas:
*   🔸HISTÓRIA DO BRASIL
*   🔸GEOGRAFIA DO BRASIL
*   🔸CIVISMO
*   🔸INFORMATICA
*   🔸ENGENHARIA CIVIL
*   🔸AGRONOMIA
*   🔸TURISMO
*   🔸ENGENHARIA ELÉTRICA
*   🔸ADMINISTRAÇÃO EMPRESARIAL
*   🔸PEDAGOGIA
*   🔸PSICANÁLISE
*   🔸JORNALISMO
*   🔸ENFERMAGEM
*   🔸NUTRIÇÃO
*   🔸EDUCAÇÃO FÍSICA
*   🔸ESPANHOL
*   🔸INGLÊS
*   🔸HEBRAICO
*   🔸GREGO
*   🔸BIOMEDICINA
*   🔸MEDICINA VETERINARIA
*   🔸ADVOCACIA
*   🔸FISIOTERAPIA
*   🔸CIBER SEGURANÇA
*   🔸ENGENHARIA MECÂNICA
*   🔸ANTROPOLOGIA
*   🔸GEOLOGIA
*   🔸PALEONTOLOGIA
*   🔸AVIAÇÃO
*   🔸ENGENHARIA FLORESTAL
---

## VERSÃO 1.4 - 16/01/2024:
* ✅Foi adicionado um sistema de validação para empedir que o usuário deixe uma questão em branco ou digite um valor inválido.
* ✅Foi corrigido o bug de fechamento inesperado do arquivo executavel.
* ✅Foi corrigido o valor da média no resultado final. Agora só exibe um valor inteiro.
* ✅Depois de exibir o resultado o programa fecha em 60 segundos (Exibe uma contagem regressiva).
---

## VERSÃO 1.3 - 21/12/2023:
* ✅Foi adicionado um `MENU PRINCIPAL`; Ao iniciar o app, o usuário poderá escolher a máteria apenas digitando o número correspondente (Já tem o sistema de validação).
* ✅17 novas máterias foram adicionadas:
    * 🔸PORTUGUES
    * 🔸MATEMATICA
    * 🔸QUIMICA
    * 🔸BIOLOGIA
    * 🔸HISTORIA
    * 🔸GEOGRAFIA
    * 🔸FILOSOFIA
    * 🔸SOCIOLOGIA
    * 🔸ARTES
    * 🔸RELIGIAO
    * 🔸LITERATURA
    * 🔸TECNOLOGIA
    * 🔸MEDICINA
    * 🔸DIREITOS
    * 🔸POLITICA
    * 🔸ECONOMIA
    * 🔸MARKETING
* ✅Depois de muito tempo, temos o prazer de anunciar o lançamento publico desse maravilhoso app para Windows X64. Se trata de um arquivo executável. Basta apenas baixar e executar.
---

## VERSÃO 1.2 - 17/08/2022:
* ✅Agora temos o encapsulamento de módulos em arquivos diferentes. Apartir de agora o código será publicado em formato de zip; Contendo: As funções de análise e um arquivo para cada materia. O aluno poderá escolher a matéria apenas dando play no arquivo com o seu nome;
* ✅Foi lançado uma breve saudação; Anuciando o nome da matéria a ser respondida;
* ✅Agora temos a função de "CARREGANDO({C}%)..." ao iniciar;
* ✅Se o usuário errar a questão, o script irá mostrar a alternativa correta;
* ✅As alternativas foram mudadas de lower(a,b,c,d) para upper(A,B,C,D);
* ✅No resultado final, ele exibe a média de acertos;
* ✅No resultado final, o algoritmo irá calcular a porcetagem de acertos e o número de questões corretas. Se os acertos forem maiores do que 70% ou o número de questões corretas forem maiores que o número de questões erradas: o aluno será aprovado; Caso contrário, será reprovado. Isso permitirá ao dono colocar mais de 10 Questões ou menos para cada materia;
* ✅Agora temos 10 Questões de Teologia.
---

## VERSÃO 1.1 - 29/06/2022:
* ✅Enquanto o usuário não enviar a resposta entre "abcd", será considerada inválida; Repetindo a mesma pergunta novamente;
* ✅Agora ele exibe "CERTA RESPOSTA" caso tenha acertado e "VOCÊ ERROU" caso tenha errado;
* ✅Foi criado uma nova função para estética do divisor entre as questões (=);
* ✅Agora temos uma breve saudação antes de começar o questionário.
* ✅Substituímos as questões de 3 até 10 de Teologia para Física volume 3;
* ✅Agora o aluno só será aprovado se acertar mais de 7 Questões.
---

## VERSÃO 1.0 - 20/06/2022:
* ✅Foi lançado hoje um algoritmo de perguntas objetivas (Como a prova do ENEM); Por enquanto seu nome é "QUESTOES" e é um projeto solo. 
* ✅Código bem organizado: A função de avaliação de resposta  está no módulo A, as questões no B, e C para o resultado final; 
* ✅Atualmente tem 10 perguntas (2 de Física e 8 de Teologia);
* ✅O usuário tem apenas uma chance para responder cada pergunta após iniciar o algoritmo;
* ✅Existe um indice da lista para respostas certas e para respostas erradas;
* ✅Modo lento de 1 sg está ativado para cada pergunta;
* ✅Por padrão ele aceita valores INT e FLOAT como respostas erradas;
* ✅Ele exibe se o usuário errou ou acertou após responder;
* ✅No final ele mostra quais foram as Questões certas e erradas (com a quantidade) junto com o resultado final se o usuário foi aprovado no teste (Apenas se os acertos forem maiores do que os erros) ou não.


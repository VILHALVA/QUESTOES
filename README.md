# QUESTOES
👨‍💻QUESTÕES É UM APP DE SIMULADOR DE ENEM QUE RODA NO CONSOLE DA IDE.

<img src="FOTO.png" align="center" width="500"> <br>

## DESCRIÇÃO:
O programa é um quiz interativo que apresenta perguntas sobre uma matéria específica. Aqui está uma descrição mais concisa:

1. **Menu principal:** O usuário poderá escolher mais de 20 matérias.

2. **Boas-vindas:** Sauda o jogador e informa sobre a matéria das perguntas.

3. **Perguntas:** Apresenta uma série de perguntas ao usuário.

4. **Respostas:** Aceita as respostas do usuário (A, B, C ou D) para cada pergunta.

5. **Feedback:** Fornece feedback imediato sobre a correção da resposta.

6. **Resultado Final:** Ao final, exibe estatísticas, incluindo questões corretas, questões erradas, quantidade de acertos, quantidade de erros, média de acertos e determina se o jogador foi aprovado ou reprovado com base em uma porcentagem mínima de acertos.

## EXECUTANDO O PROJETO:
1. Navegue até o diretório `./CODIGO`, e execute o arquivo Python com o comando:
```bash
python MAIN.py
```
2. Isso abrirá o menu principal do programa no console.
3. Leia as opções do menu e escolha a opção desejada digitando o número correspondente.
4. O programa executará a função associada à opção escolhida.
5. Após a execução da opção escolhida, o programa retornará ao menu principal, onde você pode escolher outra opção ou sair do programa digitando `0`.
6. Quando terminar de usar o programa, escolha a opção `0` para sair.

## SOBRE O EXECUTAVEL E O INSTALADOR:
### 1. EXECUTANDO:
- O instalador está disponível apenas para `Windows X64`. Para instala-lo, basta dar dois cliques e seguir as orientações na tela. 

- Este arquivo executável está disponível apenas para `Windows X64` (No diretório `APP`). Para executá-lo, basta dar dois cliques. O executável é bastante útil caso o Python não esteja instalado. Trata-se da mesma aplicação do arquivo `MAIN.py`. Se desejar, você pode recompilá-lo novamente; é para isso que forneci o arquivo `imagem.ico`.

### 2. GERANDO:
   **1. Instalação do [PyInstaller:](https://pyinstaller.org/en/stable/)**
   - Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   - Para gerar o executável, utilize o comando `pyinstaller` seguido de opções:
      - `--icon="imagem.ico"`: Especifica o ícone do executável.
      - `-F`: Gera um único arquivo executável em vez de vários.
      - `MAIN.py`: Substitua "MAIN.py" pelo nome do seu arquivo Python principal.
   ```bash
   pyinstaller --icon="imagem.ico" -F MAIN.py
   ```

### 3. GERANDO O INSTALADOR:
#### PASSO 1: BAIXAR E INSTALAR O INNO SETUP:
1. **Download**: Baixe o Inno Setup do site oficial: [Inno Setup](http://www.jrsoftware.org/isdl.php).
2. **Instalação**: Siga o assistente de instalação para instalar o Inno Setup no seu sistema.

#### PASSO 2: CRIAR O SCRIPT DO INSTALADOR:
1. **Abrir o Inno Setup**: Após a instalação, abra o Inno Setup.
2. **Novo Script**: Na tela inicial, clique em "New Script" e selecione "Next" no assistente que aparecer.
3. **Informações Básicas**:
   - **Application Information**: Preencha as informações da sua aplicação, como nome, versão, nome do publisher e website.
   - **Application Destination Base Folder**: Normalmente, você pode deixar como "{pf}\YourAppName" (para instalar no diretório de Program Files).
   - **Application Directory**: Selecione a pasta onde estão os arquivos da sua aplicação. Em `./APP` desse repositório.
   - **Application Files**: Adicione todos os arquivos necessários para a instalação da sua aplicação (executáveis, DLLs, etc).
   - **Application Shortcuts**: Escolha se deseja criar atalhos no menu Iniciar, na área de trabalho, etc.
   - **Application Documentation**: Adicione arquivos de licença e outros documentos necessários.
4. **Output**: Escolha onde o arquivo de instalação (.exe) será salvo.
5. **Create Script**: Clique em "Finish" para gerar o script base.

#### PASSO 3: EDITAR O SCRIPT:
O Inno Setup irá abrir o script gerado automaticamente. Aqui, você pode fazer ajustes se necessário. O script terá uma estrutura básica como esta:

```pascal
[Setup]
AppName=Your Application Name
AppVersion=1.0
DefaultDirName={pf}\YourAppName
DefaultGroupName=YourAppName
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Path\To\YourApp\*"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\YourAppName"; Filename: "{app}\YourApp.exe"
Name: "{commondesktop}\YourAppName"; Filename: "{app}\YourApp.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\YourApp.exe"; Description: "{cm:LaunchProgram,YourAppName}"; Flags: nowait postinstall skipifsilent
```

#### PASSO 4: COMPILAR O SCRIPT:
1. **Compilar**: Com o script aberto no Inno Setup, clique no botão "Compile" na barra de ferramentas.
2. **Verificar**: O Inno Setup irá compilar o script e criar o arquivo de instalação na pasta especificada.
3. **Testar**: Execute o instalador gerado para testar e verificar se tudo está funcionando corretamente.

#### PASSO 5: PERSONALIZAÇÕES ADICIONAIS (OPCIONAL):
Você pode adicionar customizações ao seu instalador, como adicionar telas personalizadas, verificações de pré-requisitos, etc. A documentação oficial do Inno Setup tem exemplos e explicações detalhadas para essas funcionalidades.

#### RECURSOS ÚTEIS:
- **Documentação Oficial**: [Inno Setup Documentation](http://www.jrsoftware.org/isinfo.php)
- **Exemplos de Scripts**: O Inno Setup inclui exemplos de scripts que podem ser muito úteis para entender como implementar certas funcionalidades.

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens e tecnologias, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS E MAIS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)
- [CLIQUE AQUI PARA VER O HISTÓRICO DE ATUALIZAÇÕES](./UPDATES.md)

README - Conversor de JPEG para PDF em Python

Descrição

Este sistema converte automaticamente imagens no formato JPEG para PDF sem alterar os nomes dos arquivos, apenas substituindo a extensão.

Passo a Passo para Instalação e Execução

1. Instalar o Python

Caso ainda não tenha o Python instalado, baixe e instale a versão mais recente a partir de:

Site oficial do Python

Durante a instalação, marque a opção "Add Python to PATH" para facilitar a execução dos comandos.

2. Instalar as Dependências

Abra o PowerShell e execute o seguinte comando para instalar as bibliotecas necessárias:

pip install pillow pypdf2

Se a instalação apresentar erro de conexão, tente novamente.

3. Corrigir Caminho do Python (Se Necessário)

Se ao tentar rodar o script aparecer a mensagem Python não encontrado, execute no PowerShell:

[System.Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\\Users\\rebarros\\AppData\\Local\\Programs\\Python\\Python311", [System.EnvironmentVariableTarget]::User)

Feche e reabra o PowerShell.

Se o erro persistir, desative os aliases do Python na Microsoft Store:

Vá até Configurações → Aplicativos → Aplicativos e recursos.

Clique em Gerenciar aliases de execução do aplicativo e desative o alias do Python.

4. Executar o Conversor

No PowerShell, navegue até a pasta onde está o script:

cd C:\temp\convertec_jpeg_pdf

Depois, execute o script:

python .\conv_jpeg_pdf.py

Se necessário, use o caminho completo do Python:

C:\Users\rebarros\AppData\Local\Programs\Python\Python311\python.exe .\conv_jpeg_pdf.py

Possíveis Erros e Soluções

Erro 1: Python não encontrado

Solução: Corrigir o PATH do Python conforme descrito acima.

Erro 2: Permissão negada ao acessar arquivos

Solução: Execute o PowerShell como Administrador e tente novamente.

Erro 3: Nenhuma imagem JPEG encontrada no diretório

Solução: Verifique se as imagens estão no diretório correto.

Erro 4: Falha ao instalar dependências

Solução: Verifique a conexão com a internet ou tente novamente mais tarde.

Funcionamento do Sistema

1. Identificação de Arquivos

O script percorre o diretório definido e identifica todos os arquivos .jpg e .jpeg.

2. Conversão para PDF

Cada imagem é convertida em um arquivo PDF com o mesmo nome do arquivo original.

3. Geração dos PDFs

Os arquivos PDF são gerados na mesma pasta dos arquivos de imagem originais.

Observações

O script pode ser adaptado para processar outros formatos de imagem.

Certifique-se de ter espaço suficiente no disco para armazenar os arquivos convertidos.

Caso precise converter um grande número de imagens, pode ser necessário otimizar o script para desempenho.

Este sistema facilita a conversão de imagens para PDF de forma rápida e eficiente. Qualquer dúvida ou melhoria, sinta-se à vontade para ajustar o código conforme necessário!
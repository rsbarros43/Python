README - Conversor de TXT para PDF/DOC

Descrição

Este projeto permite a conversão de arquivos de texto (TXT) para os formatos PDF ou DOCX, facilitando a geração de documentos formatados.

Dependências

Para executar o script, é necessário instalar as seguintes bibliotecas:

pip install fpdf python-docx

Como Usar

O script recebe três argumentos:

O arquivo de entrada no formato .txt.

O formato de saída desejado (pdf ou doc).

O nome do arquivo de saída.

Exemplo de Uso

Para converter um arquivo exemplo.txt para exemplo.pdf:

python script.py exemplo.txt pdf exemplo.pdf

Para converter um arquivo exemplo.txt para exemplo.docx:

python script.py exemplo.txt doc exemplo.docx

Estrutura do Projeto

├── script.py           # Script principal para conversão
├── README.TXT         # Instruções do projeto

Observações

O arquivo de entrada deve estar no formato .txt.

O formato de saída deve ser pdf ou doc.

O script verifica se o arquivo de entrada existe antes de iniciar a conversão.

Contato

Caso tenha dúvidas ou precise de suporte, entre em contato pelo e-mail: 
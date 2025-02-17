Conversor de Imagens HEIC para JPEG

Este projeto permite converter imagens no formato .HEIC para .JPEG de forma automática usando Python. Ele percorre uma pasta de entrada, converte todas as imagens HEIC e salva os arquivos no formato JPEG em uma pasta de saída.

📌 Pré-requisitos

Antes de executar o script, certifique-se de que você tem os seguintes requisitos instalados:

1️⃣ Instalar o Python

Caso ainda não tenha o Python instalado, baixe e instale a versão mais recente em:
🔗 https://www.python.org/downloads/

Obs: Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.

2️⃣ Instalar Dependências

Abra o Prompt de Comando (cmd no Windows) ou Terminal (Mac/Linux) e execute o seguinte comando:

pip install pillow pillow-heif

Isso instalará:

pillow → Biblioteca para manipulação de imagens.

pillow-heif → Permite a leitura de arquivos HEIC.

📂 Estrutura do Projeto

📁 Conversor_HEIC
│── converter_heic.py  # Script de conversão
│── README.txt  # Este arquivo de instruções
│── 📂 imagens_heic  # Pasta com as imagens HEIC a serem convertidas
│── 📂 imagens_convertidas  # Pasta onde serão salvas as imagens JPEG

📝 Como Criar o Script

1️⃣ Criar um Arquivo Python

Abra um editor de código como VS Code, PyCharm ou Bloco de Notas, e copie o seguinte código para um novo arquivo chamado converter_heic.py:

import os
from PIL import Image
import pillow_heif

# Diretório de entrada e saída
input_folder = r"C:\Users\SeuUsuario\Downloads\imagens_heic"
output_folder = r"C:\Users\SeuUsuario\Downloads\imagens_convertidas"

# Criar pasta de saída se não existir
os.makedirs(output_folder, exist_ok=True)

# Percorrer todos os arquivos HEIC na pasta de entrada
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(".heic"):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".jpg")

        # Carregar imagem HEIC
        heif_file = pillow_heif.open_heif(input_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode
        )

        # Converter e salvar como JPEG
        image.save(output_path, "JPEG", quality=90)

        print(f"✔ Convertido: {file_name} -> {output_path}")

print("✅ Conversão concluída!")

▶️ Como Executar o Script

Windows

Abra o Prompt de Comando (Win + R → digite cmd → Enter).

Navegue até a pasta onde salvou o script:

cd C:\Users\SeuUsuario\Downloads\Conversor_HEIC

Execute o script:

python converter_heic.py

Mac/Linux

Abra o Terminal.

Navegue até a pasta do script:

cd /home/seuusuario/Downloads/Conversor_HEIC

Execute o script:

python3 converter_heic.py

📌 Exemplo de Saída no Terminal

Após a execução bem-sucedida, você verá algo assim no terminal:

✔ Convertido: imagem1.heic -> C:\Users\SeuUsuario\Downloads\imagens_convertidas\imagem1.jpg
✔ Convertido: imagem2.heic -> C:\Users\SeuUsuario\Downloads\imagens_convertidas\imagem2.jpg
✔ Convertido: imagem3.heic -> C:\Users\SeuUsuario\Downloads\imagens_convertidas\imagem3.jpg
✅ Conversão concluída!

Após a conversão, suas imagens .JPEG estarão disponíveis na pasta imagens_convertidas.

🛠️ Possíveis Erros e Soluções

❌ Erro: "ModuleNotFoundError: No module named 'pillow_heif'"

🔹 Solução: Execute novamente o comando de instalação:

pip install pillow pillow-heif

❌ Erro: "FileNotFoundError: [Errno 2] No such file or directory"

🔹 Solução: Certifique-se de que a pasta imagens_heic existe e contém arquivos .HEIC.

❌ Erro: "SyntaxError: (unicode error) 'unicodeescape' codec can't decode..."

🔹 Solução: Use r"caminho" antes do diretório, por exemplo:

input_folder = r"C:\Users\SeuUsuario\Downloads\imagens_heic"

✅ Conclusão

Agora você tem um conversor de HEIC para JPEG totalmente funcional e automatizado! 🎉

Caso precise adicionar mais funcionalidades, como interface gráfica (GUI) ou upload direto para um servidor, podemos expandir o projeto! 🚀

Boa conversão! 😊
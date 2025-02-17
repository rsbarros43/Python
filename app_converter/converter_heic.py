import os
from PIL import Image
import pillow_heif

# Diretório de entrada e saída (corrigido)
input_folder = r"C:\Users\rebarros\Downloads\Avaliacao\Fotos_atual_casa"
output_folder = r"C:\Users\rebarros\Downloads\Avaliacao\Fotos_convertidas"

# Certifique-se de que o diretório de saída existe
os.makedirs(output_folder, exist_ok=True)

# Percorrer todos os arquivos no diretório de entrada
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

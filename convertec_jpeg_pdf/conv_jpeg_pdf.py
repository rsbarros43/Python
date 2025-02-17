from PIL import Image
import os

def convert_jpeg_to_pdf(input_dir):
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".jpg") or f.lower().endswith(".jpeg")]
    image_files.sort()
    
    if not image_files:
        print("Nenhuma imagem JPEG encontrada no diretório.")
        return
    
    for image_file in image_files:
        image_path = os.path.join(input_dir, image_file)
        img = Image.open(image_path).convert('RGB')
        pdf_path = os.path.splitext(image_path)[0] + ".pdf"
        img.save(pdf_path)
    
    print("Conversão concluída. PDFs gerados com sucesso.")

if __name__ == "__main__":
    input_directory = r"C:\\Users\\rebarros\\Downloads\\Avaliacao\\Prestacao_servicos_chacara"
    convert_jpeg_to_pdf(input_directory)

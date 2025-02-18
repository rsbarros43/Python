import whisper
import os

def convert_audio_to_text(audio_file):
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_file)
        return result['text']
    except Exception as e:
        print(f"Erro ao converter áudio: {e}")
        return None

def main():
    while True:
        print("\nMenu de Opções:")
        print("1 - Converter áudio para texto")
        print("2 - Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            audio_file = input("Digite o caminho do arquivo .ogg: ")
            
            if not os.path.exists(audio_file):
                print("Arquivo não encontrado! Tente novamente.")
                continue
            
            print("Convertendo áudio para texto...")
            text = convert_audio_to_text(audio_file)
            
            if text:
                print("Texto extraído:")
                print(text)
        
        elif escolha == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
2
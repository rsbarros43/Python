import os
from awr_parser import parse_awr
from report_generator import generate_awr_report

def main():
    awr_file_path = "C:/temp/awr_analyzer/input/awr_report.html"
    output_path = "C:/temp/awr_analyzer/output/awr_analysis_report.docx"

    print("\n🔄 Executando análise do AWR...\n")

    if not os.path.exists(awr_file_path):
        print(f"⚠️ Arquivo {awr_file_path} não encontrado. Verifique o caminho.")
        return

    with open(awr_file_path, "r", encoding="latin-1") as file:
        awr_html = file.read()

    parsed_awr = parse_awr(awr_html)
    
    print("\n📄 Gerando relatório...\n")
    generate_awr_report(parsed_awr, output_path)
    print(f"\n✅ Relatório gerado com sucesso: {output_path}")

if __name__ == "__main__":
    main()

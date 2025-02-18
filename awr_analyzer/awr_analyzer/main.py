from awr_analyzer.awr_parser import parse_awr
from awr_analyzer.sql_analyzer import analyze_sql_ordered_by_elapsed_time, generate_sql_recommendations
from awr_analyzer.config_analyzer import analyze_memory_config, generate_memory_recommendations
#from awr_analyzer.report_generator import generate_html_report

def main(awr_file_path):
    """
    Função principal para análise do AWR.
    """
    soup = parse_awr(awr_file_path)

    if soup is None:
        print("❌ Erro ao processar o arquivo AWR.")
        return
    
    print("\n🔍 Analisando SQLs por tempo de execução...")
    sql_df = analyze_sql_ordered_by_elapsed_time(soup)
    
    if sql_df is not None:
        sql_recommendations = generate_sql_recommendations(sql_df)
        print("\n🔎 Recomendações para SQLs problemáticos:")
        for rec in sql_recommendations:
            print(rec)

if __name__ == "__main__":
    awr_file_path = r"C:\temp\awr_analyzer\input\awr_report.html"
    main(awr_file_path)

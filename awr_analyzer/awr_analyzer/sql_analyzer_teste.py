import pandas as pd
from bs4 import BeautifulSoup
from awr_analyzer.oracle_docs import get_oracle_doc

def extract_sql_table(soup):
    if not isinstance(soup, BeautifulSoup):
        raise TypeError("Erro: 'soup' precisa ser um objeto BeautifulSoup, mas recebeu um tipo inválido.")

    table = soup.find("table", summary="This table displays top SQL by elapsed time")
    
    if not table:
        print("⚠️ Tabela 'SQL Ordered by Elapsed Time' não encontrada.")
        return []

    rows = table.find_all("tr")[1:]
    data = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 10:
            continue

        sql_id = cols[6].text.strip()
        elapsed_time = cols[0].text.strip().replace(",", "").replace(" ", "")
        cpu_time = cols[4].text.strip().replace(",", "").replace(" ", "")
        executions = cols[1].text.strip().replace(",", "").replace(" ", "")
        elapsed_per_exec = cols[2].text.strip().replace(",", "").replace(" ", "")
        sql_text = cols[9].text.strip()

        data.append([sql_id, elapsed_time, cpu_time, executions, elapsed_per_exec, sql_text])

    return data


def analyze_sql_ordered_by_elapsed_time(soup):
    data = extract_sql_table(soup)

    if not data:
        print("⚠️ Nenhum dado extraído da tabela 'SQL Ordered by Elapsed Time'.")
        return None

    df = pd.DataFrame(data, columns=['SQL ID', 'Elapsed Time (s)', 'CPU Time (s)', 'Executions', 'Elapsed per Exec (s)', 'SQL Text'])

    df['Elapsed Time (s)'] = pd.to_numeric(df['Elapsed Time (s)'], errors='coerce')
    df['CPU Time (s)'] = pd.to_numeric(df['CPU Time (s)'], errors='coerce')
    df['Executions'] = pd.to_numeric(df['Executions'], errors='coerce')
    df['Elapsed per Exec (s)'] = pd.to_numeric(df['Elapsed per Exec (s)'], errors='coerce')

    return df


def generate_sql_recommendations(df):
    if df is None or df.empty:
        print("⚠️ Nenhuma recomendação pode ser gerada pois o DataFrame está vazio.")
        return []

    recommendations = []
    for index, row in df.iterrows():
        if row['Elapsed per Exec (s)'] > 1.0:
            rec = f"🔍 SQL ID '{row['SQL ID']}' está lento (Elapsed per Exec: {row['Elapsed per Exec (s)']}s).\n"
            rec += "👉 Recomendações:\n"

            # Sugestão de índice
            rec += "✅ Verifique se há necessidade de um índice:\n"
            rec += f"```sql\nSELECT INDEX_NAME, TABLE_NAME FROM DBA_INDEXES WHERE TABLE_NAME LIKE '%{row['SQL Text'][:10]}%';\n```\n"

            # Otimização do SQL
            rec += "✅ Teste uma reescrita da query para melhorar performance.\n"

            # Link da Oracle
            rec += f"📚 Documentação: {get_oracle_doc('sql_tuning')}\n"

            recommendations.append(rec)

    return recommendations

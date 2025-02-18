# Caminho base
$basePath = "C:\temp\awr_analyzer"

# Criar diretórios
New-Item -Path "$basePath\awr_analyzer" -ItemType Directory
New-Item -Path "$basePath\input" -ItemType Directory
New-Item -Path "$basePath\output" -ItemType Directory
New-Item -Path "$basePath\templates" -ItemType Directory

# Criar arquivos Python
@"
from bs4 import BeautifulSoup

def parse_awr(file_path):
    \"\"\"
    Parseia o arquivo AWR (HTML) e retorna um objeto BeautifulSoup.
    \"\"\"
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    return soup

def extract_section(soup, section_title):
    \"\"\"
    Extrai uma seção específica do relatório AWR.
    \"\"\"
    section = soup.find('h2', text=section_title)
    if not section:
        return None
    table = section.find_next('table')
    if not table:
        return None
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        if cols:
            data.append([col.text.strip() for col in cols])
    return data
"@ | Out-File -FilePath "$basePath\awr_analyzer\awr_parser.py" -Encoding UTF8

@"
import pandas as pd

def analyze_sql_ordered_by_elapsed_time(data):
    \"\"\"
    Analisa a seção 'SQL Ordered by Elapsed Time' do AWR.
    \"\"\"
    df = pd.DataFrame(data, columns=['SQL ID', 'Elapsed Time (s)', 'CPU Time (s)', 'Executions', 'Elapsed per Exec (s)', 'SQL Text'])
    df['Elapsed Time (s)'] = df['Elapsed Time (s)'].astype(float)
    df['CPU Time (s)'] = df['CPU Time (s)'].astype(float)
    df['Elapsed per Exec (s)'] = df['Elapsed per Exec (s)'].astype(float)
    return df

def generate_sql_recommendations(df):
    \"\"\"
    Gera recomendações para SQLs problemáticos.
    \"\"\"
    recommendations = []
    for index, row in df.iterrows():
        if row['Elapsed per Exec (s)'] > 1.0:  # Exemplo de threshold
            recommendations.append(
                f\"SQL ID '{row['SQL ID']}' está lento (Elapsed per Exec: {row['Elapsed per Exec (s)']}s). \"
                \"Considere otimizar a query, verificar índices ou reescrever o SQL.\"
            )
    return recommendations

def suggest_indexes(sql_text):
    \"\"\"
    Sugere criação de índices com base no texto do SQL.
    \"\"\"
    suggestions = []
    if \"WHERE\" in sql_text:
        suggestions.append(\"Considere criar um índice nas colunas usadas na cláusula WHERE.\")
    if \"JOIN\" in sql_text:
        suggestions.append(\"Considere criar índices nas colunas usadas em JOINS.\")
    return suggestions
"@ | Out-File -FilePath "$basePath\awr_analyzer\sql_analyzer.py" -Encoding UTF8

@"
def analyze_memory_config(soup):
    \"\"\"
    Analisa a configuração de memória (PGA, SGA) do banco de dados.
    \"\"\"
    memory_section = soup.find('h2', text='Memory Statistics').find_next('table')
    rows = memory_section.find_all('tr')
    memory_data = {}
    for row in rows:
        cols = row.find_all('td')
        if len(cols) == 2:
            key = cols[0].text.strip()
            value = cols[1].text.strip()
            memory_data[key] = value
    return memory_data

def generate_memory_recommendations(memory_data):
    \"\"\"
    Gera recomendações para ajustes de memória (PGA, SGA, etc.).
    \"\"\"
    recommendations = []
    pga_aggregate_target = int(memory_data.get('PGA Aggregate Target', '0').replace(',', ''))
    sga_target = int(memory_data.get('SGA Target', '0').replace(',', ''))
    
    if pga_aggregate_target < 1024 * 1024 * 1024:  # 1GB
        recommendations.append(
            \"O valor de 'PGA Aggregate Target' está baixo. Considere aumentar para melhorar o desempenho de operações em memória.\"
        )
    if sga_target < 2 * 1024 * 1024 * 1024:  # 2GB
        recommendations.append(
            \"O valor de 'SGA Target' está baixo. Considere aumentar para melhorar o cache de dados e desempenho geral.\"
        )
    return recommendations
"@ | Out-File -FilePath "$basePath\awr_analyzer\config_analyzer.py" -Encoding UTF8

@"
from jinja2 import Template

def generate_html_report(recommendations, output_file='output/awr_analysis_report.html'):
    \"\"\"
    Gera um relatório HTML com as recomendações.
    \"\"\"
    template = Template(\"\"\"
    <html>
    <head><title>Relatório de Análise AWR</title></head>
    <body>
        <h1>Recomendações</h1>
        <ul>
        {% for rec in recommendations %}
            <li>{{ rec }}</li>
        {% endfor %}
        </ul>
    </body>
    </html>
    \"\"\")
    html_content = template.render(recommendations=recommendations)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)
"@ | Out-File -FilePath "$basePath\awr_analyzer\report_generator.py" -Encoding UTF8

@"
from awr_parser import parse_awr, extract_section
from sql_analyzer import analyze_sql_ordered_by_elapsed_time, generate_sql_recommendations, suggest_indexes
from config_analyzer import analyze_memory_config, generate_memory_recommendations
from report_generator import generate_html_report

def main(awr_file_path):
    # Parseia o arquivo AWR
    soup = parse_awr(awr_file_path)
    
    # Analisa SQLs problemáticos
    sql_data = extract_section(soup, 'SQL Ordered by Elapsed Time')
    sql_df = analyze_sql_ordered_by_elapsed_time(sql_data)
    sql_recommendations = generate_sql_recommendations(sql_df)
    
    # Sugere índices para SQLs problemáticos
    for index, row in sql_df.iterrows():
        sql_text = row['SQL Text']
        index_suggestions = suggest_indexes(sql_text)
        sql_recommendations.extend(index_suggestions)
    
    # Analisa configuração de memória
    memory_data = analyze_memory_config(soup)
    memory_recommendations = generate_memory_recommendations(memory_data)
    
    # Gera o relatório HTML
    all_recommendations = sql_recommendations + memory_recommendations
    generate_html_report(all_recommendations)
    print(\"Relatório gerado com sucesso em 'output/awr_analysis_report.html'.\")

if __name__ == \"__main__\":
    awr_file_path = 'input/awr_report.html'  # Caminho para o arquivo AWR
    main(awr_file_path)
"@ | Out-File -FilePath "$basePath\awr_analyzer\main.py" -Encoding UTF8

# Criar arquivo requirements.txt
@"
beautifulsoup4==4.12.0
pandas==2.0.3
Jinja2==3.1.2
"@ | Out-File -FilePath "$basePath\requirements.txt" -Encoding UTF8

# Criar arquivo README.md
#@"
# AWR Analyzer

#Um software em Python para análise de relatórios AWR do Oracle.

## Como funciona

#O aplicativo faz o seguinte:
#1. Parseia o arquivo AWR (HTML).
#2. Identifica SQLs problemáticos (lentos, com alto consumo de CPU, etc.).
#3. Analisa a configuração de memória (PGA, SGA).
#4. Gera recomendações para otimização.
#5. Cria um relatório HTML com as recomendações.

## Como usar

#1. Instale as dependências:

#   ```bash
#   pip install -r requirements.txt
def analyze_memory_config(soup):
    """
    Analisa a configuração de memória (PGA, SGA) do banco de dados.
    """
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
    """
    Gera recomendações para ajustes de memória (PGA, SGA, etc.).
    """
    recommendations = []
    pga_aggregate_target = int(memory_data.get('PGA Aggregate Target', '0').replace(',', ''))
    sga_target = int(memory_data.get('SGA Target', '0').replace(',', ''))
    
    if pga_aggregate_target < 1024 * 1024 * 1024:  # 1GB
        recommendations.append(
            "O valor de 'PGA Aggregate Target' está baixo. Considere aumentar para melhorar o desempenho de operações em memória."
        )
    if sga_target < 2 * 1024 * 1024 * 1024:  # 2GB
        recommendations.append(
            "O valor de 'SGA Target' está baixo. Considere aumentar para melhorar o cache de dados e desempenho geral."
        )
    return recommendations

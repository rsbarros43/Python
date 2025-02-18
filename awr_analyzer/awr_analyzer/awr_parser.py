from bs4 import BeautifulSoup

def parse_awr(awr_html):
    """Extrai os dados do relatório AWR e retorna um dicionário estruturado."""
    soup = BeautifulSoup(awr_html, 'html.parser')
    awr_data = {}

    print("\n🔎 Iniciando a extração de dados do AWR...\n")

    # 🔍 CPU Usage
    cpu_section = soup.find("h2", string=lambda text: text and "Host CPU" in text)
    if cpu_section:
        table = cpu_section.find_next("table")
        rows = table.find_all("tr")[1:] if table else []
        cpu_data = [[col.text.strip() for col in row.find_all("td")] for row in rows]
        awr_data["CPU Usage"] = cpu_data if cpu_data else [["N/A"]]
        print("✅ CPU Usage extraído com sucesso.")
    else:
        awr_data["CPU Usage"] = [["Seção não encontrada"]]
        print("⚠️ Não foi possível encontrar a seção 'Host CPU Usage'.")

    # 🔍 PGA Usage
    pga_section = soup.find("h2", string=lambda text: text and "Memory Statistics" in text)
    if pga_section:
        table = pga_section.find_next("table")
        rows = table.find_all("tr") if table else []
        pga_data = [[col.text.strip() for col in row.find_all("td")] for row in rows if len(row.find_all("td")) >= 2]
        awr_data["PGA Usage"] = pga_data if pga_data else [["N/A", "N/A"]]
        print("✅ PGA Usage extraído com sucesso.")
    else:
        awr_data["PGA Usage"] = [["Seção não encontrada", "N/A"]]
        print("⚠️ Não foi possível encontrar a seção 'Memory Statistics'.")

    # 🔍 Wait Events
    wait_events_section = soup.find("h2", string=lambda text: text and "Top Timed Events" in text)
    if wait_events_section:
        table = wait_events_section.find_next("table")
        rows = table.find_all("tr")[1:] if table else []
        wait_events = [[col.text.strip() for col in row.find_all("td")] for row in rows if len(row.find_all("td")) >= 6]
        awr_data["Wait Events"] = wait_events if wait_events else [["N/A"]]
        print("✅ Wait Events extraído com sucesso.")
    else:
        awr_data["Wait Events"] = [["Seção não encontrada"]]
        print("⚠️ Não foi possível encontrar a seção 'Top Timed Events'.")

    # 🔍 SQL Offenders
    sql_section = soup.find("h2", string=lambda text: text and "SQL Ordered by Elapsed Time" in text)
    if sql_section:
        table = sql_section.find_next("table")
        rows = table.find_all("tr")[1:] if table else []
        sql_offenders = [[col.text.strip() for col in row.find_all("td")] for row in rows if len(row.find_all("td")) >= 9]
        awr_data["SQL Offenders"] = sql_offenders if sql_offenders else [["N/A"]]
        print("✅ SQL Offenders extraído com sucesso.")
    else:
        awr_data["SQL Offenders"] = [["Seção não encontrada"]]
        print("⚠️ Não foi possível encontrar a seção 'SQL Ordered by Elapsed Time'.")

    # 🔍 ADDM Findings
    addm_section = soup.find("h2", string=lambda text: text and "ADDM Findings" in text)
    if addm_section:
        table = addm_section.find_next("table")
        rows = table.find_all("tr")[1:] if table else []
        addm_findings = [[col.text.strip() for col in row.find_all("td")] for row in rows if len(row.find_all("td")) >= 3]
        awr_data["ADDM Findings"] = addm_findings if addm_findings else [["N/A"]]
        print("✅ ADDM Findings extraído com sucesso.")
    else:
        awr_data["ADDM Findings"] = [["Seção não encontrada"]]
        print("⚠️ Não foi possível encontrar a seção 'ADDM Findings'.")

    return awr_data

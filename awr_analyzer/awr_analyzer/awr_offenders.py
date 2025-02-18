from bs4 import BeautifulSoup

def extract_offenders(soup):
    """
    Extrai todas as seções importantes do relatório AWR.
    """
    sections = {}

    # CPU Usage
    cpu_section = soup.find("h2", text="Host CPU Usage")
    if cpu_section:
        sections["CPU Usage"] = cpu_section.find_next("table").prettify()

    # IO Performance
    io_section = soup.find("h2", text="IO Profile")
    if io_section:
        sections["IO Profile"] = io_section.find_next("table").prettify()

    # Locks & Contention
    lock_section = soup.find("h2", text="Enqueue Activity")
    if lock_section:
        sections["Lock Contention"] = lock_section.find_next("table").prettify()

    # Memory Usage
    memory_section = soup.find("h2", text="Memory Statistics")
    if memory_section:
        sections["Memory Usage"] = memory_section.find_next("table").prettify()

    return sections

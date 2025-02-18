AWR Analyzer

Este aplicativo permite analisar arquivos AWR (Automatic Workload Repository) da Oracle e gerar um relatório detalhado em .docx contendo: ✅ SQLs problemáticos e recomendações de otimização

✅ Uso de CPU, I/O, locks e paralelismo
✅ Plano de Ação com ações e scripts SQL sugeridos
✅ Links oficiais da Oracle para otimização

Ele é projetado para facilitar a análise de desempenho e tuning de bancos de dados Oracle de forma automatizada, entregando insights tanto técnicos quanto gerenciais.

📌 1. Instalação
Antes de rodar o script, certifique-se de que possui o Python 3.11+ instalado.

1️⃣ Clone o repositório (ou copie os arquivos para uma pasta de trabalho):


git clone https://github.com/seu-repositorio/awr_analyzer.git
cd awr_analyzer

2️⃣ Instale as dependências necessárias:


pip install -r requirements.txt

📌 2. Estrutura de Diretórios
O projeto possui a seguinte estrutura:

📂 C:\temp\awr_analyzer\
│── 📂 awr_analyzer\
│   │── __init__.py
│   │── awr_offenders.py        # Analisador de ofensores do AWR (CPU, I/O, Locks, etc.)
│   │── awr_parser.py           # Parser para extrair informações do HTML do AWR
│   │── config_analyzer.py       # Analisador de configuração de memória (SGA, PGA)
│   │── main.py                  # Script principal que roda a análise
│   │── oracle_docs.py           # Módulo com links da documentação oficial da Oracle
│   │── report_generator.py      # Gera o relatório final em .docx
│   │── run_analysis.py          # Script para executar todo o processo automaticamente
│   │── sql_analyzer.py          # Identifica SQLs lentos e gera recomendações
│
│── 📂 input\  
│   │── awr_report.html          # Arquivo AWR a ser analisado (copiar para esta pasta)
│
│── 📂 output\  
│   │── awr_analysis_report.docx # Relatório gerado após a análise
│
│── requirements.txt             # Dependências do projeto
│── README.txt                   # Este arquivo com a documentação do projeto

📌 3. Como Rodar o Programa
Para rodar a análise do AWR e gerar o relatório, siga os passos abaixo:

1️⃣ Copie o arquivo AWR (awr_report.html) para a pasta input/

2️⃣ Execute o script principal:

python run_analysis.py

ou no PowerShell:

python -m awr_analyzer.run_analysis

3️⃣ O relatório final será salvo em:

📁 C:/temp/awr_analyzer/output/awr_analysis_report.docx

📌 4. Funcionalidades
🔍 Análise de SQLs Problemáticos

    Identifica SQLs mais lentos e sugere reescritas e índices
    Traz links oficiais da Oracle para tuning avançado

🔥 Uso de CPU & I/O

    Detecta consultas com alto consumo de CPU
    Analisa queries com uso excessivo de disco (I/O)

🔒 Locks e Contenção

    Identifica sessões bloqueadas e queries que estão causando esperas
    Sugere scripts SQL para investigação

⚡ Paralelismo & Memória

    Verifica queries que não estão otimizadas para paralelismo
    Analisa SGA e PGA para identificar gargalos

📊 Plano de Ação Personalizado

Para cada problema identificado, o relatório gera:

✅ Descrição detalhada do problema
✅ Ofensores (SQL IDs)
✅ Ação recomendada
✅ Scripts SQL para investigação
✅ Documentação Oracle para referência

📌 5. Possíveis Erros e Soluções

🚨 Erro: No such file or directory: 'input/awr_report.html'
✔ Solução: Copie o arquivo AWR para a pasta input/ antes de rodar o script.

🚨 Erro: UnicodeDecodeError: 'utf-8' codec can't decode byte
✔ Solução: O arquivo AWR pode estar em outro encoding. Tente salvar como UTF-8.

🚨 Erro: PermissionError: [Errno 13] Permission denied: 'output/awr_analysis_report.docx'
✔ Solução: Feche o arquivo awr_analysis_report.docx antes de rodar o script novamente.

📌 6. Próximos Passos
Se precisar de ajustes ou melhorias, você pode:

1️⃣ Rodar um novo AWR e validar se todas as métricas estão sendo extraídas corretamente
2️⃣ Ajustar os parâmetros de análise para incluir mais detalhes no relatório
3️⃣ Personalizar a estrutura do relatório conforme as necessidades do cliente

Caso tenha sugestões de melhorias, abra um issue no repositório! 🚀📊

🔎 Com este script, a análise de AWR se torna automatizada e eficiente, trazendo insights detalhados para otimizar a performance dos bancos de dados Oracle.

📌 Desenvolvido por: Renato Barros
📧 Contato: rsbarros43@hotmail.com
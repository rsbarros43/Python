def get_oracle_doc(topic):
    """
    Retorna links da documentação oficial da Oracle para cada tópico de otimização.
    """
    oracle_docs = {
        "sql_tuning": "https://docs.oracle.com/en/database/oracle/oracle-database/19/tgsql/",
        "index_tuning": "https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-indexes.html",
        "parallelism": "https://docs.oracle.com/en/database/oracle/oracle-database/19/dwhsg/parallel-execution.html",
        "memory_tuning": "https://docs.oracle.com/en/database/oracle/oracle-database/19/tgsql/tuning-memory.html",
    }
    return oracle_docs.get(topic, "https://docs.oracle.com/en/database/oracle/")

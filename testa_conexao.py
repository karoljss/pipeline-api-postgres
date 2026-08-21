import psycopg2
import pandas as pd

# Parâmetros de conexão configurados no docker-compose.yml
HOST = "localhost"
PORT = "5432"
DATABASE = "engenharia_dados"
USER = "admin"
PASSWORD = "adminpassword"

try:
    # 1. Abre a conexão com o PostgreSQL
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        database=DATABASE,
        user=USER,
        password=PASSWORD
    )
    print("✅ Conexão com o PostgreSQL realizada com sucesso!")

    # 2. Executa uma consulta simples para validar
    query = "SELECT version();"
    df = pd.read_sql(query, conn)
    
    print("\n🐘 Versão do PostgreSQL rodando no Docker:")
    print(df.iloc[0, 0])

    # 3. Fecha a conexão
    conn.close()
    print("\n🔒 Conexão encerrada com segurança.")

except Exception as e:
    print(f"❌ Erro ao conectar ao banco de dados: {e}")
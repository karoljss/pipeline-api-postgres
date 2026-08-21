import pandas as pd
from sqlalchemy import create_engine

# Conexão com o banco PostgreSQL no Docker
USER = "admin"
PASSWORD = "adminpassword"
HOST = "localhost"
PORT = "5432"
DATABASE = "engenharia_dados"

DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

def consultar_cotacoes():
    engine = create_engine(DATABASE_URL)
    
    # Consulta SQL selecionando os dados gravados no banco
    query = "SELECT * FROM cotacoes_moedas ORDER BY data_coleta DESC;"
    
    df = pd.read_sql(query, con=engine)
    
    print("📌 Registros armazenados na tabela 'cotacoes_moedas':")
    print(df)

if __name__ == "__main__":
    consultar_cotacoes()
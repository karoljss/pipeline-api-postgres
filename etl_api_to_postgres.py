import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# 1. Configuração do Banco de Dados no Docker
USER = "admin"
PASSWORD = "adminpassword"
HOST = "localhost"
PORT = "5432"
DATABASE = "engenharia_dados"

# String de conexão do SQLAlchemy (Padrão de Mercado)
DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

def extrair_dados_api():
    """Extrai cotações de moedas em tempo real de uma API pública."""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("✅ Dados extraídos com sucesso da API!")
        return response.json()
    else:
        raise Exception(f"❌ Erro ao acessar API: {response.status_code}")

def transformar_dados(dados_json):
    """Trata o JSON retornado e converte para um DataFrame organizado."""
    lista_cotacoes = []
    
    for moeda, info in dados_json.items():
        lista_cotacoes.append({
            "moeda": info["code"],
            "nome": info["name"],
            "valor_compra": float(info["bid"]),
            "valor_venda": float(info["ask"]),
            "variacao": float(info["varBid"]),
            "data_coleta": datetime.now()
        })
    
    df = pd.DataFrame(lista_cotacoes)
    return df

def carregar_dados_postgres(df):
    """Salva o DataFrame formatado em uma tabela no PostgreSQL."""
    engine = create_engine(DATABASE_URL)
    
    # Salva os dados na tabela 'cotacoes_moedas' (cria a tabela automaticamente se não existir)
    df.to_sql("cotacoes_moedas", con=engine, if_exists="append", index=False)
    print("✅ Dados salvos com sucesso na tabela 'cotacoes_moedas' no PostgreSQL!")

if __name__ == "__main__":
    try:
        print("🚀 Iniciando Pipeline ETL...")
        json_bruto = extrair_dados_api()
        df_tratado = transformar_dados(json_bruto)
        print("\n📊 Prévia dos dados tratados:")
        print(df_tratado[['moeda', 'nome', 'valor_compra', 'data_coleta']])
        
        carregar_dados_postgres(df_tratado)
        print("\n🎉 Pipeline executado com 100% de sucesso!")
        
    except Exception as e:
        print(f"\n❌ Falha na execução do Pipeline: {e}")
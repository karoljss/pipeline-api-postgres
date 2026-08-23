from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Configurações padrão da DAG
default_args = {
    'owner': 'karoljss',
    'depends_on_past': False,
    'start_date': datetime(2026, 8, 20),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='dag_orquestracao_cotacoes',
    default_args=default_args,
    description='Pipeline de extração da API para o PostgreSQL no Docker',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Tarefa 1: Checa se o container PostgreSQL está rodando
    validar_banco = BashOperator(
        task_id='validar_container_postgres',
        bash_command='docker ps | grep postgres_lab',
    )

    # Tarefa 2: Executa o script de ETL
    executar_etl = BashOperator(
        task_id='executar_etl_api',
        bash_command='python /home/karolaine/pipeline-api-postgres/etl_api_to_postgres.py',
    )

    # Definição do fluxo de dependência
    validar_banco >> executar_etl
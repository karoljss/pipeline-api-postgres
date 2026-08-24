from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

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

    # Tarefa 1: Checa se o container PostgreSQL está respondendo
    validar_banco = BashOperator(
        task_id='validar_container_postgres',
        bash_command='docker ps | grep postgres_lab',
    )

    # Tarefa 2: Executa o script de ETL a partir da pasta espelhada do container
    executar_etl = BashOperator(
        task_id='executar_etl_api',
        bash_command='python /opt/airflow/dags/etl_api_to_postgres.py',
    )

    # Definição do fluxo de dependência (Acíclico e Dirigido)
    validar_banco >> executar_etl
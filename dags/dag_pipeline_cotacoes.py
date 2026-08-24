from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'karoljss',
    'depends_on_past': False,
    'start_date': datetime(2026, 8, 20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'dag_pipeline_cotacoes',
    default_args=default_args,
    description='Orquestração do pipeline de cotações',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    validar_banco = BashOperator(
        task_id='validar_container_postgres',
        bash_command='echo "Validando conexao com a infraestrutura..."',
    )

    executar_etl = BashOperator(
        task_id='executar_etl_api',
        bash_command='echo "Executando carga de dados no pipeline..."',
    )

    validar_banco >> executar_etl
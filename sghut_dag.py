from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from sghut_ETL import run_sghut_ETL

default_args = {
    'owner': 'pop',
    'depends_on_past': False,
    'start_date': datetime(2023, 2, 8),
    'email': ['mohamed.ehab.mohamed.rashad@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'sghut_dag',
    default_args=default_args,
    description='DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='complete_sghut_etl',
    python_callable=run_sghut_ETL,
    dag=dag, 
)

run_etl
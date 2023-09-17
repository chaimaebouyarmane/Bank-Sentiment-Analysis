# import the libraries
from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator  # Import PostgresOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'chaimae',
    'start_date': days_ago(0),
    'email': ['c.bouyarmane@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG
dag = DAG(
    'Bank_process',
    default_args=default_args,
    description='Process CIH Bank comment',
    start_date=datetime(2023,5,24,2),
    schedule_interval='@daily',
)
# define the tasks

extract = BashOperator(
                task_id = 'extract',
                bash_command = "python /home/project/extraction.py",
                dag=dag,
        )
transform = BashOperator(
                task_id = 'transform',
                bash_command = "python /home/project/transformation.py",
                dag=dag,
        )
truncate = PostgresOperator(
                task_id = 'truncate_table',
                postgres_conn_id = 'cbouyarmane',
                sql = "DELETE FROM banques;",
                dag=dag,
        )
load = BashOperator(
                task_id = 'load',
                bash_command = "python /home/project/loading.py",
                dag = dag,
        )
# task pipeline

extract >> transform >> truncate >> load
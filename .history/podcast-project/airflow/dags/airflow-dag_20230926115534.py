from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from function import *


# Define your DAG's default arguments
default_args = {
    'owner': 'Anh Minh',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 15),
    'retries': 1,
}

# Create the Airflow DAG
dag = DAG(
    'podcast_summary',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    catchup=False,
)


# Define the tasks
create_database = PythonOperator(
    python_callable=create_database,
    dag=dag,
)

get_episodes = PythonOperator(
    task_id='get_episodes',
    python_callable=get_episodes,
    dag=dag,
)

load_episodes = PythonOperator(
    task_id='load_episodes',
    python_callable=load_episodes,
    dag=dag,
)

download_episodes = PythonOperator(
    task_id='download_episodes',
    python_callable=download_episodes,
    dag=dag,
    op_args=[get_episodes],
)

# Set the dependencies
create_database >> get_episodes >> load_episodes >> download_episodes
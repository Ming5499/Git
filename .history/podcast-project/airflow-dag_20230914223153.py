from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from function import create_database, get_episodes_task, load_episodes_task, download_episodes_task, speech_to_text_task

# Define your DAG's default arguments
default_args = {
    'owner': 'Anh Minh',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 14),
    'retries': 1,
}

# Create the Airflow DAG
dag = DAG(
    'podcast_summary',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  # @daily
    catchup=False,
)

# Define your tasks using PythonOperator
create_database_task = PythonOperator(
    task_id='create_database_task',
    python_callable=create_database,
    dag=dag,
)

get_episodes_task = PythonOperator(
    task_id='get_episodes_task',
    python_callable=get_episodes_task,
    dag=dag,
)

load_episodes_task = PythonOperator(
    task_id='load_episodes_task',
    python_callable=load_episodes_task,
    op_args=[get_episodes_task.output],  # Define input dependencies if needed
    dag=dag,
)

download_episodes_task = PythonOperator(
    task_id='download_episodes_task',
    python_callable=download_episodes_task,
    op_args=[get_episodes_task.output],  # Define input dependencies if needed
    dag=dag,
)

speech_to_text_task = PythonOperator(
    task_id='speech_to_text_task',
    python_callable=speech_to_text_task,
    op_args=[download_episodes_task.output, load_episodes_task.output],  # Define input dependencies if needed
    dag=dag,
)

# Set task dependencies
#create_database_task >> get_episodes_task >> [load_episodes_task, download_episodes_task] >> speech_to_text_task
get_episodes_task
import os
import json
import requests
import xmltodict

from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


PODCAST_URL = "https://www.marketplace.org/feed/podcast/marketplace/"
EPISODE_FOLDER = "episodes"
FRAME_RATE = 16000


def create_database():
    create_database = PostgresOperator(
        task_id='create_table_postgres',
        sql="""
        CREATE TABLE IF NOT EXISTS episodes (
            link TEXT PRIMARY KEY,
            title TEXT,
            filename TEXT,
            published TEXT,
            description TEXT,
            transcript TEXT
        );
        """,
        postgres_conn_id="podcasts"  #PostgreSQL connection ID that connected
    )
    return create_database


def get_episodes():
    data = requests.get(PODCAST_URL)
    feed = xmltodict.parse(data.text)
    episodes = feed["rss"]["channel"]["item"]
    print(f"Found {len(episodes)} episodes.")
    return episodes


# Define your DAG's default arguments
default_args = {
    'owner': 'Anh Minh',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 15),
    'retries': 1,
}

# Create the Airflow DAG
dag = DAG(
    'podcast_summary2',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  
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
    python_callable=get_episodes,
    dag=dag,
)

create_database_task >> get_episodes_task
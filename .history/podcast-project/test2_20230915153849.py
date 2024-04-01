import os
import json
import requests
import xmltodict
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


PODCAST_URL = "https://www.marketplace.org/feed/podcast/marketplace/"
EPISODE_FOLDER = "episodes"


def create_database():
    """Creates the `episodes` table in the `podcasts` database."""
    conn = PostgresHook(postgres_conn_id="podcasts")
    conn.run("""
        CREATE TABLE IF NOT EXISTS episodes (
            link TEXT PRIMARY KEY,
            title TEXT,
            filename TEXT,
            published TEXT,
            description TEXT,
            transcript TEXT
        );
        """)

def get_episodes():
    data = requests.get(PODCAST_URL)
    feed = xmltodict.parse(data.text)
    episodes = feed["rss"]["channel"]["item"]
    print(f"Found {len(episodes)} episodes.")
    return episodes


def load_episodes(episodes):
    hook = PostgresHook(postgres_conn_id="podcasts")
    stored_episodes = hook.get_pandas_df("SELECT * from episodes;")
    new_episodes = []
    for episode in episodes:
        if episode["link"] not in stored_episodes["link"].values:
            filename = f"{episode['link'].split('/')[-1]}.mp3"
            new_episodes.append([episode["link"], episode["title"], episode["pubDate"], episode["description"], filename])

    hook.insert_rows(table='episodes', rows=new_episodes, target_fields=["link", "title", "published", "description", "filename"])
    return new_episodes


def download_episodes(episodes):
    audio_files = []
    for episode in episodes:
        name_end = episode["link"].split('/')[-1]
        filename = f"{name_end}.mp3"
        audio_path = os.path.join(EPISODE_FOLDER, filename)
        if not os.path.exists(audio_path):
            print(f"Downloading {filename}")
            audio = requests.get(episode["enclosure"]["@url"])
            with open(audio_path, "wb+") as f:
                f.write(audio.content)
            audio_files.append({
                "link": episode["link"],
                "filename": filename
            })
    return audio_files


from airflow import DAG

from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta


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
    task_id='create_database',
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
    
)

# Set the dependencies
create_database >> get_episodes >> load_episodes >> download_episodes

from function import *
from airflow.decorators import dag
from datetime import datetime, timedelta

# Define your DAG's default arguments
default_args = {
    'owner': 'Anh Minh',
    'depends_on_past': False,
    'start_date': datetime.datetime(2023, 9, 14),
    'retries': 1,
}

    
# Create the Airflow DAG
dag = DAG(
    'podcast_summary',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  # @daily
    catchup=False,

    
    create_database = create_database_task()
    podcast_episodes = get_episodes_task()
    new_episodes = load_episodes_task(podcast_episodes)
    audio_files = download_episodes_task(podcast_episodes)
    speech_to_text_task(audio_files, new_episodes)
)
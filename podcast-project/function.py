import os
import json
import requests
import xmltodict
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


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
    if not os.path.exists("episodes"):
        os.mkdir("episodes")

def get_episodes():
    data = requests.get(PODCAST_URL)
    feed = xmltodict.parse(data.text)
    episodes = feed["rss"]["channel"]["item"]
    print(f"Found {len(episodes)} episodes.")
    return episodes

def load_episodes(episodes=[]):
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
    for episode in episodes:
        name_end = episode["link"].split('/')[-1]
        filename = f"{name_end}.mp3"
        audio_path = os.path.join(EPISODE_FOLDER, filename)
        if not os.path.exists(audio_path):
            print(f"Downloading {filename}")
            audio = requests.get(episode["enclosure"]["@url"])
            with open(audio_path, "wb+") as f:
                f.write(audio.content)
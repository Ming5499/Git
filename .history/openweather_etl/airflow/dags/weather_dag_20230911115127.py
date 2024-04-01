from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.http.sensors.http import HttpSensor


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023,11,9),
    'email':['npam5499@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

with DAG('weather_dag',
        default_args = default_args,
        schedule_interval = '@daily',
        catchup=False) as dag:
        
        
        #Check weather API is available
        is_weather_api_ready = HttpSensor(
            task_id = 'is_weather_api_ready',
            http_conn_id = 'weathermap_api',
            endpoint = '/data/2.5/weather?q=hanoi&appid=fce40c3ad84e88aba9f09388dc5ca04e'
        )
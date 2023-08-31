import requests
import json
import boto3
import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import datetime

start_date = airflow.utils.dates.days_ago(2) # 2 days ago

defauls_args = {
    "owner": "anhminh",
    "depends_on_past": False,
    "email": ["npam5499@gmail.com"],
    "email_on_failure": False,
    "email_on_retry":False,
    "retries":1,
    "retry_delay":datetime.timedelta(minutes=5),
}

def json_scraper(url, file_name, bucket):
    response = requests.request("GET",url)
    json_data = response.json()
    
    with open(file_name,'w',encoding='utf8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
        
    s3.= boto3.client('s3')
    s3.upload_file(file_name,bucket, f"predictit/{file_name}")
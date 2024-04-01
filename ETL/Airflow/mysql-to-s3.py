import datetime
from airflow import DAG
from airflow.providers.mysql.operators.mysql_to_csv import MySqlToCsvOperator
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalToS3Operator
from airflow.models import Variable

# Define your DAG's default arguments
default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime.datetime(2023, 9, 14),
    'retries': 1,
}

# Create the Airflow DAG
dag = DAG(
    'mysql_to_s3_etl',
    default_args=default_args,
    schedule_interval=None,  # You can set a schedule if needed
    catchup=False,
    max_active_runs=1,
)

# Define your MySQL connection
mysql_conn_id = 'your_mysql_connection'

# Define the MySQL table to extract data from
mysql_table = 'your_source_table'

# Define the local file path to temporarily store the extracted data
local_file_path = '/tmp/extracted_data.csv'

# Define the S3 bucket and key where you want to store the data
s3_bucket = 'your_s3_bucket'
s3_key = 'your_s3_key/data.csv'

# Task to extract data from MySQL and save it locally
extract_task = MySqlToCsvOperator(
    task_id='extract_data_from_mysql',
    mysql_conn_id=mysql_conn_id,
    sql=f'SELECT * FROM {mysql_table}',
    export_dir=local_file_path,
    field_delimiter=',',
    dag=dag,
)

# Task to load data from the local file to S3
load_to_s3_task = LocalToS3Operator(
    task_id='load_data_to_s3',
    local_path=local_file_path,
    s3_bucket=s3_bucket,
    s3_key=s3_key,
    replace=True,  # Set to True if you want to replace the existing file
    aws_conn_id='your_aws_connection',
    task_concurrency=1,  # Set to control concurrency if needed
    verify=True,  # Set to False if SSL verification is not required
    bucket_name_in_s3=True,  # If s3_key should be treated as a full path
    dag=dag,
)

# Set task dependencies
extract_task >> load_to_s3_task

if __name__ == "__main__":
    dag.cli()

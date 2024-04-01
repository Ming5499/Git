import datetime
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.amazon.aws.transfers.postgres_to_s3 import PostgresToS3Operator
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
    'postgresql_to_s3_etl',
    default_args=default_args,
    schedule_interval=None,  # You can set a schedule if needed
    catchup=False,
    max_active_runs=1,
)

# Define your PostgreSQL connection
postgres_conn_id = 'your_postgres_connection'

# Define your AWS S3 connection
aws_conn_id = 'your_aws_connection'

# Define the SQL query to extract data from PostgreSQL
sql_query = """
    SELECT * FROM your_source_table
"""

# Define the S3 bucket and key where you want to store the data
s3_bucket = 'your_s3_bucket'
s3_key = 'your_s3_key/data.csv'

# Task to extract data from PostgreSQL
extract_task = PostgresOperator(
    task_id='extract_data_from_postgres',
    postgres_conn_id=postgres_conn_id,
    sql=sql_query,
    dag=dag,
)

# Task to transform and load data into S3
transform_and_load_task = PostgresToS3Operator(
    task_id='transform_and_load_to_s3',
    sql=sql_query,  # You can specify a different query for transformation if needed
    postgres_conn_id=postgres_conn_id,
    aws_conn_id=aws_conn_id,
    bucket_name=s3_bucket,
    dest_s3_key=s3_key,
    replace=True,  # Set to True if you want to replace the existing file
    dag=dag,
)

# Set task dependencies
extract_task >> transform_and_load_task

if __name__ == "__main__":
    dag.cli()

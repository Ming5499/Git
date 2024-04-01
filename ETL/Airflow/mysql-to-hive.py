import datetime
from airflow import DAG
from airflow.providers.mysql.operators.mysql_to_hive import MySqlToHiveTransfer
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
    'mysql_to_hive_etl',
    default_args=default_args,
    schedule_interval=None,  # You can set a schedule if needed
    catchup=False,
    max_active_runs=1,
)

# Define your MySQL connection
mysql_conn_id = 'your_mysql_connection'

# Define the MySQL table to extract data from
mysql_table = 'your_source_table'

# Define the target Hive table where you want to load the data
hive_table = 'your_hive_table'

# Task to extract data from MySQL and load it into Hive
extract_and_load_task = MySqlToHiveTransfer(
    task_id='extract_and_load_to_hive',
    mysql_conn_id=mysql_conn_id,
    sql=f'SELECT * FROM {mysql_table}',
    hive_table=hive_table,
    create=True,  # Set to True if the Hive table needs to be created
    delimiter=',',  # Set the delimiter as needed
    field_names=['col1', 'col2', 'col3'],  # Specify column names as per your MySQL table
    hive_cli_conn_id='your_hive_connection',  # Hive connection
    mapred_queue='your_mapred_queue',  # Set your MapReduce queue if needed
    dag=dag,
)

if __name__ == "__main__":
    dag.cli()

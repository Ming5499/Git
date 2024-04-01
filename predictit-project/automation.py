# Import libraries required for connecting to mysql
import mysql
import db2
import psycopg2
# Import libraries required for connecting to DB2 or PostgreSql

# Connect to DB2 or PostgreSql
dsn_hostname = '127.0.0.1'
dsn_user = 'postgres'
dsn_password = '123456'
dsn_port = '5432'
dsn_database = 'postgres'

# create connection
conn = psycopg2.connect(
	database = dsn_database,
	user = dsn_user,
	password = dsn_password,
	host = dsn_hostname,
	port = dsn_port
 
)
# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.

def get_last_rowid():
	cursor = conn.cursor()
	sql = "SELECT rowid FROM public.sale_data ORDER BY rowid DESC LIMIT 1"
	cursor.execute(sql)
	rows = cursor.fetchall()
	return rows[0]
last_row_id = get_last_rowid()
print(last_row_id)


last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
	pass	

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 or PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database or PostgreSql.

def insert_records(records):
	pass

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse

# disconnect from DB2 or PostgreSql data warehouse 

# End of program
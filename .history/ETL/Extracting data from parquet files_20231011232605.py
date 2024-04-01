import pandas as pd
import sqlalchemy

# Read the sales data into a DataFrame
sales_data = pd.read_parquet("sales_data.parquet", engine="fastparquet")

# Check the data type of the columns of the DataFrames
print(sales_data.dtypes)

# Print the shape of the DataFrame, as well as the head
print(sales_data.shape)
print(sales_data.head())

# Create a connection to the sales database
db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/sales")

# Query all rows and columns of the sales table
raw_sales_data = pd.read_sql("SELECT * FROM sales", db_engine)
print(raw_sales_data)

def extract():
  	# Create a connection URI and connection engine
    connection_uri = "postgresql+psycopg2://repl:password@localhost:5432/sales"
    db_engine = sqlalchemy.create_engine(connection_uri)
    # Query the DataFrame to return all records with quantity_ordered equal to 1
    raw_sales_data = pd.read_sql("SELECT * FROM sales WHERE quantity_ordered = 1", db_engine)
    
    # Print the head of the DataFrame
    print(raw_sales_data.head())
    
    # Return the extracted DataFrame
    return raw_sales_data
    
# Call the extract() function
raw_sales_data = extract()

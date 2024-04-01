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

#Extracting data from parquet files
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

----------------------------------------------------------------------------------------------------
# Extract data from the sales_data.parquet path
raw_sales_data = extract("sales_data.parquet")

def transform(raw_data):
  	# Only keep rows with `quantity` greater than 1
    clean_data = raw_data.loc[raw_data["Quantity Ordered"] > 1, :]
	
    # Only keep columns "Order Date", "Quantity Ordered", and "Purchase Address"
    clean_data = clean_data.loc[:, ["Order Date", "Quantity Ordered", "Purchase Address"]]
	
    # Return the filtered DataFrame
    return clean_data
    
transform(raw_sales_data)


def transform2(raw_data):
    # Convert the "Order Date" column to type datetime
    raw_data["Order Date"] = pd.to_datetime(raw_data["Order Date"], format="%m/%d/%y %H:%M")
    
    # Only keep items under ten dollars
    clean_data = raw_data.loc[raw_data["Price Each"] < 10, :]
    clean_data2 = raw_data.loc[raw_data["Quantity Ordered"] == 1, ["Order ID", "Price Each", "Quantity Ordered"]]
    return clean_data, clean_data2

clean_sales_data = transform2(raw_sales_data)

# Check the data types of each column
print(clean_sales_data.dtypes)


----------------------------------------------------------------------------------------------------

# Import the os library
import os

# Load the data to a csv file with the index, no header and pipe separated
def load(clean_data, path_to_write):
	return clean_data.to_csv(path_to_write, header=False, sep="|")
  
load(clean_sales_data, "clean_sales_data.csv")

# Check that the file is present.
file_exists = os.path.exists("clean_sales_data.csv")
print(file_exists)

def load2(clean_data, file_path):
    # Write the data to a file
    clean_data.to_csv(file_path, header =False, index = False)

    # Check to make sure the file exists
    file_exists = os.path.exists(file_path)
    if not file_exists:
        raise Exception(f"File does NOT exists at path {file_path}")

# Load the transformed data to the provided file path
load2(clean_sales_data, "transformed_sales_data.csv")


------------------------------------------------------------------------------------
import logging

def transform(raw_data):
    raw_data["Order Date"] = pd.to_datetime(raw_data["Order Date"], format="%m/%d/%y %H:%M")
    clean_data = raw_data.loc[raw_data["Price Each"] < 10, :]
    
    # Create an info log regarding transformation
    logging.info("Transformed 'Order Date' column to type 'datetime'.")
    
    # Log the dimension of the DataFrame before and after filtering
    logging.debug(f"Shape of the DataFrame before filtering: {raw_data.shape}")
    logging.debug(f"Shape of DataFrame after filtering: {clean_data.shape}")
    
    return clean_data
  
clean_sales_data = transform(raw_sales_data)

----------------------------------------------------------------------------------------------------
import json

def extract(file_path):
  # Read the JSON file into a DataFrame
  return pd.read_json(file_path, orient="records")

# Call the extract function with the appropriate path, assign to raw_testing_scores
raw_testing_scores = extract("testing_scores.json")

# Output the head of the DataFrame
print(raw_testing_scores.head())
-----------------------------------------------------------------------------------
# Import the json library
import json

def extract(file_path):
    with open(file_path, "r") as json_file:
        # Load the data from the JSON file
        raw_data = json.load(json_file)
    return raw_data

raw_testing_scores = extract("nested_scores.json")

# Print the raw_testing_scores
print(raw_testing_scores)
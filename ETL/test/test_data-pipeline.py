# Validating a data pipeline at "checkpoints"

# Extract and transform tax_data
raw_tax_data = extract("raw_tax_data.csv")
clean_tax_data = transform(raw_tax_data)

# Check the shape of the raw_tax_data DataFrame, compare to the clean_tax_data DataFrame
print(f"Shape of raw_tax_data: {raw_tax_data.shape}")
print(f"Shape of clean_tax_data: {clean_tax_data.shape}")

# Read in the loaded data, observe the head of each
to_validate = pd.read_parquet("clean_tax_data.parquet")
print(clean_tax_data.head(3))
print(to_validate.head(3))

# Check that the DataFrames are equal
print(to_validate.equals(clean_tax_data))

######################################################################################
# Trigger the data pipeline to run three times
for attempt in range(0, 3):
	print(f"Attempt: {attempt}")
	raw_tax_data = extract("raw_tax_data.csv")
	clean_tax_data = transform(raw_tax_data)
	load(clean_tax_data, "clean_tax_data.parquet")
	
	# Print the shape of the cleaned_tax_data DataFrame
	print(f"Shape of clean_tax_data: {clean_tax_data.shape}")
    
# Read in the loaded data, check the shape
to_validate = pd.read_parquet("clean_tax_data.parquet")
print(f"Final shape of cleaned data: {to_validate.shape}")

##################################################################################
# Validating a data pipeline with assert and isinstance
raw_tax_data = extract("raw_tax_data.csv")
clean_tax_data = transform(raw_tax_data)

# Assert that clean_tax_data is an instance of a pd.DataFrame
assert isinstance(clean_tax_data, pd.DataFrame)

# Assert that clean_tax_data takes is an instance of a string
try: 
	assert isinstance(clean_tax_data, str)
except Exception as e:
	print(e)


# Writing unit tests with pytest
import pytest

def test_transformed_data():
    raw_tax_data = extract("raw_tax_data.csv")
    clean_tax_data = transform(raw_tax_data)
    
    # Assert that the transform function returns a pd.DataFrame
    assert isinstance(clean_tax_data, pd.DataFrame)
    
    # Assert that the clean_tax_data DataFrame has more columns than the raw_tax_data DataFrame
    assert len(clean_tax_data.columns) > len(raw_tax_data.columns)
    

# Import pytest
import pytest

def extract(file_path):
    return pd.read_csv(file_path)

# Create a pytest fixture
@pytest.fixture()
def raw_tax_data():
	raw_data = extract("raw_tax_data.csv")
   
    # Return the raw DataFrame
	return raw_data

# Define a pytest fixture
@pytest.fixture()
def clean_tax_data():
    raw_data = pd.read_csv("raw_tax_data.csv")
    
    # Transform the raw_data, store in clean_data DataFrame, and return the variable
    clean_data = transform(raw_data)
    return clean_data

# Pass the fixture to the function
def test_tax_rate(clean_tax_data):
    # Assert values are within the expected range
    assert clean_tax_data["tax_rate"].max() <= 1 and clean_tax_data["tax_rate"].min() >= 0


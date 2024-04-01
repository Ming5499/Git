#Iterating over dictionaries
raw_testing_scores_keys = []
raw_testing_scores_values = []

# Iterate through the values of the raw_testing_scores dictionary
for school_id, school_info in raw_testing_scores.items():
	raw_testing_scores_keys.append(school_id)
	raw_testing_scores_values.append(school_info)

print(raw_testing_scores_keys[0:3])
print(raw_testing_scores_values[0:3])

#######################################################
# Parsing data from dictionaries
school = {
    "street_address": "111 Columbia Street",
    "city": "Manhattan",
    "scores": {
        "math": 657,
        "reading": 601
    }
}

# Parse the street_address from the dictionary
street_address = school.get("street_address")

# Parse the scores dictionary
scores = school.get("scores")

# Try to parse the math, reading and writing values from scores
math_score = scores.get("math", 0)
reading_score = scores.get("reading", 0)
writing_score = scores.get("writing", 0)

print(f"Street Address: {street_address}")
print(f"Math: {math_score}, Reading: {reading_score}, Writing: {writing_score}")

# Street Address: 111 Columbia Street
# Math: 657, Reading: 601, Writing: 0

# Transforming JSON data
normalized_testing_scores = []

# Loop through each of the dictionary key-value pairs
for school_id, school_info in raw_testing_scores.items():
	normalized_testing_scores.append([
    	school_id,
    	school_info.get("street_address"),  # Pull the "street_address"
    	school_info.get("city"),
    	school_info.get("scores").get("math", 0),
    	school_info.get("scores").get("reading", 0),
    	school_info.get("scores").get("writing", 0),
    ])

print(normalized_testing_scores)

# Transforming and cleaning DataFrames
# Create a DataFrame from the normalized_testing_scores list
normalized_data = pd.DataFrame(normalized_testing_scores)

# Set the column names
normalized_data.columns = ["school_id", "street_address", "city", "avg_score_math", "avg_score_reading", "avg_score_writing"]

normalized_data = normalized_data.set_index("school_id")
print(normalized_data.head())

#Filling missing values with pandas
# Print the head of the `raw_testing_scores` DataFrame
print(raw_testing_scores.head())
#               street_address       city  math_score  reading_score  writing_score
# 02M260  425 West 33rd Street  Manhattan         NaN            NaN            NaN
# 06M211    650 Academy Street  Manhattan         NaN            NaN            NaN
# 01M539   111 Columbia Street  Manhattan       657.0          601.0          601.0
# 02M294      350 Grand Street  Manhattan       395.0          411.0          387.0
# 02M308      350 Grand Street  Manhattan       418.0          428.0          415.0

# Fill NaN values with the average from that column
raw_testing_scores["math_score"] = raw_testing_scores["math_score"].fillna(raw_testing_scores["math_score"].mean())

def transform(raw_data):
	raw_data.fillna(
    	value={
			# Fill NaN values with column mean
			"math_score": raw_data["math_score"].mean(),
			"reading_score": raw_data["reading_score"].mean(),
			"writing_score": raw_data["writing_score"].mean()
		}, inplace=True
	)
	return raw_data

clean_testing_scores = transform(raw_testing_scores)

# Print the head of the clean_testing_scores DataFrame
print(clean_testing_scores.head())

# Grouping data with pandas
#               street_address       city  math_score  reading_score  writing_score
# 01M539   111 Columbia Street  Manhattan       657.0          601.0          601.0
# 02M294      350 Grand Street  Manhattan       395.0          411.0          387.0
# 02M308      350 Grand Street  Manhattan       418.0          428.0          415.0

def transform(raw_data):
	# Use .loc[] to only return the needed columns
	raw_data = raw_data.loc[:, ["city", "math_score", "reading_score", "writing_score"]]
	
    # Group the data by city, return the grouped DataFrame
	grouped_data = raw_data.groupby(by=["city"], axis=0).mean()
	return grouped_data

# Transform the data, print the head of the DataFrame
grouped_testing_scores = transform(raw_testing_scores)
print(grouped_testing_scores.head())


#Applying advanced transformations to DataFrames	
def transform(raw_data):
	# Use the apply function to extract the street_name from the street_address
    raw_data["street_name"] = raw_data.apply(
    	# Pass the correct function to the apply method
        find_street_name,
        axis=1
    )
    return raw_data

# Transform the raw_testing_scores DataFrame
cleaned_testing_scores = transform(raw_testing_scores)

# Print the head of the cleaned_testing_scores DataFrame
print(cleaned_testing_scores.head())


# Loading data to a Postgres database
# Update the connection string, create the connection object to the schools database
db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/schools")

# Write the DataFrame to the scores_by_city table
cleaned_testing_scores.to_sql(
	name="scores",
	con=db_engine,
	index=False,
	if_exists="replace"
)

# Validating data loaded to a Postgres Database
def load(clean_data, con_engine):
	# Store the data in the schools database
    clean_data.to_sql(
    	name="scores_by_city",
		con=con_engine,
		if_exists="replace",  # Make sure to replace existing data
		index=True,
		index_label="school_id"
    )

def load(clean_data, con_engine):
    clean_data.to_sql(name="scores_by_city", con=con_engine, if_exists="replace", index=True, index_label="school_id")
    
# Call the load function, passing in the cleaned DataFrame
load(cleaned_testing_scores, db_engine)

# Call query the data in the scores_by_city table, check the head of the DataFrame
to_validate = pd.read_sql("SELECT * FROM scores_by_city", con=db_engine)
print(to_validate.head())

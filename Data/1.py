from sqlalchemy import create_engine
engine = create_engine('sqlite:///census_nyc.sqlite')
connection = engine.connect()
print(engine.table_names())

from sqlalchemy import MetaData, Table
metadata = MetaData()
census = Table('census', metadata,autoload=True,autoload_with=engine)
print(repr(census))

from sqlalchemy import create_engine
engine = create_engine('sqlite:///census_nyc.sqlite')
stmt = 'SELECT * FROM people'
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()

# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by accessing it by its index
print(first_row[0])

# Print the state column of the first row by using its name
print(first_row['state'])
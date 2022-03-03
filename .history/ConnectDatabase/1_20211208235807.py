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
from pyspark.sql import SparkSession
from pyspark.sql.functions import rand

spark = SparkSession.builder.appName("FakeDataGenerator").getOrCreate()
num_rows = 50
fake_data = spark.range(num_rows).select(rand().alias("id"), rand().alias("value"))
print(fake_data)

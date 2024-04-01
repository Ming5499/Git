# CLEANING DATA
# Read a csv file and set the headers
df = (spark.read
      .options(header=True)
      .csv("/home/repl/workspace/mnt/data_lake/landing/ratings.csv"))

df.show()

# Define the schema
schema = StructType([
  StructField("brand", StringType(), nullable=False),
  StructField("model", StringType(), nullable=False),
  StructField("absorption_rate", ByteType(), nullable=True),
  StructField("comfort", ByteType(), nullable=True)
])

better_df = (spark
             .read
             .options(header="true")
             # Pass the predefined schema to the Reader
             .schema(schema)
             .csv("/home/repl/workspace/mnt/data_lake/landing/ratings.csv"))
pprint(better_df.dtypes)


# Specify the option to drop invalid rows
ratings = (spark
           .read
           .options(header=True, mode="DROPMALFORMED")
           .csv("/home/repl/workspace/mnt/data_lake/landing/ratings_with_invalid_rows.csv"))
ratings.show()
####################################################################################
print("BEFORE")
ratings.show()

print("AFTER")
# Replace nulls with arbitrary value on column subset
ratings = ratings.fillna(4, subset=["comfort"])
ratings.show()

BEFORE
+------------+-------+---------------+-------+
|       brand|  model|absorption_rate|comfort|
+------------+-------+---------------+-------+
|Diapers-R-Us|6months|              2|      3|
|     Nappy-k|2months|              3|      4|
|     Pampers|3months|              4|      4|
|     Huggies|newborn|              3|      5|
|     Pampers|    2mo|           null|   null|
+------------+-------+---------------+-------+

AFTER
+------------+-------+---------------+-------+
|       brand|  model|absorption_rate|comfort|
+------------+-------+---------------+-------+
|Diapers-R-Us|6months|              2|      3|
|     Nappy-k|2months|              3|      4|
|     Pampers|3months|              4|      4|
|     Huggies|newborn|              3|      5|
|     Pampers|    2mo|           null|      4|
+------------+-------+---------------+-------+

#############################################################################
from pyspark.sql.functions import col, when

# Add/relabel the column
categorized_ratings = ratings.withColumn(
    "comfort",
    # Express the condition in terms of column operations
    when(col("comfort") > 3, "sufficient").otherwise("insufficient"))

categorized_ratings.show()
+------------+-------+---------------+------------+
|       brand|  model|absorption_rate|     comfort|
+------------+-------+---------------+------------+
|Diapers-R-Us|6months|              2|insufficient|
|     Nappy-k|2months|              3|  sufficient|
|     Pampers|3months|              4|  sufficient|
|     Huggies|newborn|              3|  sufficient|
+------------+-------+---------------+------------+



######################################################################
#TRANSFORMING DATA

from pyspark.sql.functions import col

# Select the columns and rename the "absorption_rate" column
result = ratings.select([col("brand"),
                       col("model"),
                       col("absorption_rate").alias("absorbency")])

# Show only unique values
result.distinct().show()
+------------+-------+----------+
|       brand|  model|absorbency|
+------------+-------+----------+
|     Pampers|3months|         4|
|Diapers-R-Us|6months|         2|
|     Huggies|newborn|         3|
|     Nappy-k|2months|         3|

######################################################################
# Grouping and aggregating data
from pyspark.sql.functions import col, avg, stddev_samp, max as sfmax

aggregated = (purchased
              # Group rows by 'Country'
              .groupBy(col('Country'))
              .agg(
                # Calculate the average salary per group
                avg('Salary').alias('average_salary'),
                # Calculate the standard deviation per group and rename
                stddev_samp('Salary'),
                # Retain the highest salary per group and rename
                sfmax('Salary').alias('highest_salary')
              )
             )

aggregated.show()
+-------+--------------+-------------------+--------------+
|Country|average_salary|stddev_samp(Salary)|highest_salary|
+-------+--------------+-------------------+--------------+
|Germany|       63000.0|                NaN|         63000|
| France|       48000.0|                NaN|         48000|
|  Spain|       62000.0| 12727.922061357855|         71000|
+-------+--------------+-------------------+--------------+
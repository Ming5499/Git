import pandas as pd

df = pd.read_parquet('C:/Users/Admin/Desktop/Project-DE/Uber/fhvhv_tripdata_2021-01.parquet')
df.to_csv('C:/Users/Admin/Desktop/Project-DE/Uber/fhvhv_tripdata_2021-01.csv')
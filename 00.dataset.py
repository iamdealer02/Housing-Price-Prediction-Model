import os
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Correct environment variable
os.environ["KAGGLEHUB_CACHE"] = "D:/Machine-Learning/HousePrice prediction/data"

file_path = "Housing.csv"

df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "yasserh/housing-prices-dataset",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)
print("First 5 records:", df.head())

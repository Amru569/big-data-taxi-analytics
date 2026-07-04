import os
import sys

python_path = sys.executable

# Force Spark to use the current virtual environment Python
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("Spark Test")
    .config("spark.pyspark.python", python_path)
    .config("spark.pyspark.driver.python", python_path)
    .getOrCreate()
)

print("=" * 60)
print("Driver Python :", python_path)
print("Python Version:", sys.version)
print("Spark Version :", spark.version)
print("=" * 60)

data = [
    ("John", 25),
    ("Alice", 30),
    ("Bob", 35),
]

df = spark.createDataFrame(data, ["Name", "Age"])
df.show()

spark.stop()
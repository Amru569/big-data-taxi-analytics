import os
import sys

from pyspark.sql import SparkSession


def create_spark_session():
    """
    Create and return a Spark Session.
    """

    python_path = sys.executable

    os.environ["PYSPARK_PYTHON"] = python_path
    os.environ["PYSPARK_DRIVER_PYTHON"] = python_path

    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("Big Data Taxi Analytics")
        .config("spark.driver.memory", "4g")
        .config("spark.sql.shuffle.partitions", "8")
        .config("spark.pyspark.python", python_path)
        .config("spark.pyspark.driver.python", python_path)
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    return spark
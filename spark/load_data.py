from pyspark.sql import DataFrame

from spark.spark_session import create_spark_session


class TaxiDataLoader:
    """
    Loads NYC Taxi Dataset.
    """

    def __init__(self, file_path: str):

        self.file_path = file_path

        self.spark = create_spark_session()

    def load(self) -> DataFrame:

        df = self.spark.read.parquet(self.file_path)

        return df
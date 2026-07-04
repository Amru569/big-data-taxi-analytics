from pyspark.sql import DataFrame
from pyspark.sql.functions import col


class TaxiCleaner:
    """
    Cleans NYC Taxi Dataset.
    """

    def __init__(self, dataframe: DataFrame):

        self.df = dataframe

    def clean(self):

        df = self.df

        # Remove NULL values
        df = df.dropna()

        # Passenger count must be greater than 0
        df = df.filter(
            col("passenger_count") > 0
        )

        # Trip distance must be positive
        df = df.filter(
            col("trip_distance") > 0
        )

        # Fare amount must be positive
        df = df.filter(
            col("fare_amount") > 0
        )

        # Total amount must be positive
        df = df.filter(
            col("total_amount") > 0
        )

        return df
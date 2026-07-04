from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    hour,
    dayofmonth,
    month,
    year,
    dayofweek,
    unix_timestamp,
    when
)


class FeatureEngineer:
    """
    Creates useful features from raw taxi trip data.
    """

    def __init__(self, dataframe: DataFrame):

        self.df = dataframe

    def transform(self):

        df = self.df

        # Trip Duration (Minutes)
        df = df.withColumn(
            "trip_duration_minutes",
            (
                unix_timestamp(col("tpep_dropoff_datetime"))
                -
                unix_timestamp(col("tpep_pickup_datetime"))
            ) / 60
        )

        # Pickup Hour
        df = df.withColumn(
            "pickup_hour",
            hour("tpep_pickup_datetime")
        )

        # Pickup Day
        df = df.withColumn(
            "pickup_day",
            dayofmonth("tpep_pickup_datetime")
        )

        # Pickup Month
        df = df.withColumn(
            "pickup_month",
            month("tpep_pickup_datetime")
        )

        # Pickup Year
        df = df.withColumn(
            "pickup_year",
            year("tpep_pickup_datetime")
        )

        # Day of Week
        df = df.withColumn(
            "day_of_week",
            dayofweek("tpep_pickup_datetime")
        )

        # Weekend Flag
        df = df.withColumn(
            "is_weekend",
            when(
                col("day_of_week").isin(1, 7),
                "Yes"
            ).otherwise("No")
        )

        return df
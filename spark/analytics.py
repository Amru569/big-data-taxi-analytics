from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    avg,
    sum,
    count,
    desc,
    round
)


class TaxiAnalytics:
    """
    Performs Business Analytics on NYC Taxi Dataset.
    """

    def __init__(self, dataframe: DataFrame):

        self.df = dataframe

    # ---------------------------------------------------
    # Overall KPIs
    # ---------------------------------------------------

    def total_trips(self):

        return self.df.count()

    def total_revenue(self):

        revenue = (

            self.df

            .select(
                round(sum("total_amount"), 2)
            )

            .collect()[0][0]

        )

        return revenue

    def average_fare(self):

        fare = (

            self.df

            .select(
                round(avg("fare_amount"), 2)
            )

            .collect()[0][0]

        )

        return fare

    def average_trip_distance(self):

        distance = (

            self.df

            .select(
                round(avg("trip_distance"), 2)
            )

            .collect()[0][0]

        )

        return distance

    def average_trip_duration(self):

        duration = (

            self.df

            .select(
                round(avg("trip_duration_minutes"), 2)
            )

            .collect()[0][0]

        )

        return duration

    # ---------------------------------------------------
    # Peak Hours
    # ---------------------------------------------------

    def peak_hours(self):

        return (

            self.df

            .groupBy("pickup_hour")

            .agg(
                count("*").alias("Total Trips")
            )

            .orderBy(desc("Total Trips"))

        )

    # ---------------------------------------------------
    # Payment Distribution
    # ---------------------------------------------------

    def payment_distribution(self):

        return (

            self.df

            .groupBy("payment_type")

            .agg(
                count("*").alias("Trips")
            )

            .orderBy(desc("Trips"))

        )

    # ---------------------------------------------------
    # Pickup Locations
    # ---------------------------------------------------

    def top_pickup_locations(self):

        return (

            self.df

            .groupBy("PULocationID")

            .agg(
                count("*").alias("Trips")
            )

            .orderBy(desc("Trips"))

        )

    # ---------------------------------------------------
    # Dropoff Locations
    # ---------------------------------------------------

    def top_dropoff_locations(self):

        return (

            self.df

            .groupBy("DOLocationID")

            .agg(
                count("*").alias("Trips")
            )

            .orderBy(desc("Trips"))

        )

    # ---------------------------------------------------
    # Pickup Zones
    # ---------------------------------------------------

    def top_pickup_zones(self):

        return (

            self.df

            .groupBy("Pickup_Zone")

            .agg(
                count("*").alias("Trips")
            )

            .orderBy(desc("Trips"))

        )

    # ---------------------------------------------------
    # Dropoff Zones
    # ---------------------------------------------------

    def top_dropoff_zones(self):

        return (

            self.df

            .groupBy("Dropoff_Zone")

            .agg(
                count("*").alias("Trips")
            )

            .orderBy(desc("Trips"))

        )
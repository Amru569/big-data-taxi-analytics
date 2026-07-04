from pyspark.sql import DataFrame


class TaxiLookupJoiner:
    """
    Joins Taxi Dataset with Taxi Zone Lookup Table.
    """

    def __init__(self, spark):

        self.spark = spark

    def load_lookup(self, csv_path):

        lookup = (

            self.spark.read

            .option("header", True)

            .csv(csv_path)

        )

        return lookup

    def join_pickup(self, trips, lookup):

        pickup_lookup = (

            lookup

            .withColumnRenamed("LocationID", "PULocationID")

            .withColumnRenamed("Borough", "Pickup_Borough")

            .withColumnRenamed("Zone", "Pickup_Zone")

            .withColumnRenamed("service_zone", "Pickup_Service_Zone")

        )

        return trips.join(

            pickup_lookup,

            on="PULocationID",

            how="left"

        )

    def join_dropoff(self, trips, lookup):

        drop_lookup = (

            lookup

            .withColumnRenamed("LocationID", "DOLocationID")

            .withColumnRenamed("Borough", "Dropoff_Borough")

            .withColumnRenamed("Zone", "Dropoff_Zone")

            .withColumnRenamed("service_zone", "Dropoff_Service_Zone")

        )

        return trips.join(

            drop_lookup,

            on="DOLocationID",

            how="left"

        )
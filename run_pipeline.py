from spark.load_data import TaxiDataLoader
from spark.clean_data import TaxiCleaner
from spark.transform import FeatureEngineer
from spark.join_lookup import TaxiLookupJoiner
from spark.analytics import TaxiAnalytics

# -----------------------------------------------------
# Dataset Paths
# -----------------------------------------------------

FILE_PATH = "data/raw/yellow_tripdata_2026-01.parquet"

LOOKUP_PATH = "data/raw/taxi_zone_lookup.csv"

# -----------------------------------------------------
# Load Dataset
# -----------------------------------------------------

print("=" * 70)
print("BIG DATA TAXI ANALYTICS PLATFORM")
print("=" * 70)

loader = TaxiDataLoader(FILE_PATH)

df = loader.load()

print("\nOriginal Rows")
print(df.count())

# -----------------------------------------------------
# Clean Dataset
# -----------------------------------------------------

cleaner = TaxiCleaner(df)

clean_df = cleaner.clean()

print("\nCleaned Rows")
print(clean_df.count())

print("\nRows Removed")
print(df.count() - clean_df.count())

# -----------------------------------------------------
# Feature Engineering
# -----------------------------------------------------

engineer = FeatureEngineer(clean_df)

feature_df = engineer.transform()

# -----------------------------------------------------
# Join Taxi Lookup Dataset
# -----------------------------------------------------

joiner = TaxiLookupJoiner(loader.spark)

lookup = joiner.load_lookup(LOOKUP_PATH)

feature_df = joiner.join_pickup(
    feature_df,
    lookup
)

feature_df = joiner.join_dropoff(
    feature_df,
    lookup
)

print("\nJoined Dataset Preview")

feature_df.select(

    "Pickup_Zone",

    "Dropoff_Zone",

    "fare_amount",

    "trip_distance"

).show(10, truncate=False)

# -----------------------------------------------------
# Analytics
# -----------------------------------------------------

analytics = TaxiAnalytics(feature_df)

print("\n")
print("=" * 70)
print("BUSINESS ANALYTICS")
print("=" * 70)

print("\nTotal Trips")
print(analytics.total_trips())

print("\nTotal Revenue")
print(analytics.total_revenue())

print("\nAverage Fare")
print(analytics.average_fare())

print("\nAverage Trip Distance")
print(analytics.average_trip_distance())

print("\nAverage Trip Duration")
print(analytics.average_trip_duration())

# -----------------------------------------------------
# Peak Hours
# -----------------------------------------------------

print("\n")
print("=" * 70)
print("PEAK HOURS")
print("=" * 70)

analytics.peak_hours().show(10)

# -----------------------------------------------------
# Payment Distribution
# -----------------------------------------------------

print("\n")
print("=" * 70)
print("PAYMENT DISTRIBUTION")
print("=" * 70)

analytics.payment_distribution().show()

# -----------------------------------------------------
# Top Pickup IDs
# -----------------------------------------------------

print("\n")
print("=" * 70)
print("TOP PICKUP LOCATION IDs")
print("=" * 70)

analytics.top_pickup_locations().show(10)

# -----------------------------------------------------
# Top Dropoff IDs
# -----------------------------------------------------

print("\n")
print("=" * 70)
print("TOP DROPOFF LOCATION IDs")
print("=" * 70)

analytics.top_dropoff_locations().show(10)

# -----------------------------------------------------
# Top Pickup Zones
# -----------------------------------------------------

print("\n")
print("=" * 70)
print("TOP PICKUP ZONES")
print("=" * 70)

analytics.top_pickup_zones().show(10, truncate=False)

# -----------------------------------------------------
# Top Dropoff Zones
# -----------------------------------------------------

print("\n")
print("=" * 70)
print("TOP DROPOFF ZONES")
print("=" * 70)

analytics.top_dropoff_zones().show(10, truncate=False)

# -----------------------------------------------------
# Close Spark
# -----------------------------------------------------

loader.spark.stop()

print("\n")
print("=" * 70)
print("SPARK SESSION CLOSED SUCCESSFULLY")
print("=" * 70)
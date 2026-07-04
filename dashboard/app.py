import os
import sys
import streamlit as st

# ==========================================================
# Fix Python Path
# ==========================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ==========================================================
# Project Imports
# ==========================================================

from spark.load_data import TaxiDataLoader
from spark.clean_data import TaxiCleaner
from spark.transform import FeatureEngineer
from spark.join_lookup import TaxiLookupJoiner
from spark.analytics import TaxiAnalytics
from spark.cache_manager import CacheManager

from dashboard.dashboard_utils import spark_to_pandas
from dashboard.charts import DashboardCharts

# ==========================================================
# Streamlit Configuration
# ==========================================================

st.set_page_config(
    page_title="NYC Taxi Analytics",
    page_icon="🚖",
    layout="wide"
)

# ==========================================================
# Dataset Paths
# ==========================================================

FILE_PATH = "data/raw/yellow_tripdata_2026-01.parquet"
LOOKUP_PATH = "data/raw/taxi_zone_lookup.csv"

# ==========================================================
# Cache Spark Pipeline
# ==========================================================

@st.cache_resource
def load_pipeline():

    loader = TaxiDataLoader(FILE_PATH)

    # Load Dataset
    df = loader.load()

    # Clean Dataset
    clean_df = TaxiCleaner(df).clean()

    # Feature Engineering
    feature_df = FeatureEngineer(clean_df).transform()

    # Join Lookup Table
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

    # Cache Spark DataFrame
    feature_df = CacheManager.cache(feature_df)

    analytics = TaxiAnalytics(feature_df)

    return loader, analytics


# ==========================================================
# Load Everything
# ==========================================================

loader, analytics = load_pipeline()

# ==========================================================
# Dashboard Title
# ==========================================================

st.title("🚖 Big Data Taxi Analytics Platform")

st.markdown(
    "### Apache Spark + Streamlit + Plotly Dashboard"
)

st.divider()

# ==========================================================
# KPI Cards
# ==========================================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🚖 Total Trips",
    f"{analytics.total_trips():,}"
)

col2.metric(
    "💰 Total Revenue",
    f"${analytics.total_revenue():,.2f}"
)

col3.metric(
    "💵 Average Fare",
    f"${analytics.average_fare():,.2f}"
)

col4.metric(
    "📏 Avg Distance",
    f"{analytics.average_trip_distance()} miles"
)

st.divider()

# ==========================================================
# Peak Hours
# ==========================================================

st.subheader("🕒 Peak Pickup Hours")

peak_df = spark_to_pandas(
    analytics.peak_hours()
)

st.plotly_chart(
    DashboardCharts.peak_hour_chart(peak_df),
    width="stretch"
)

# ==========================================================
# Payment Distribution
# ==========================================================

st.subheader("💳 Payment Distribution")

payment_df = spark_to_pandas(
    analytics.payment_distribution()
)

st.plotly_chart(
    DashboardCharts.payment_chart(payment_df),
    width="stretch"
)

# ==========================================================
# Pickup Zones
# ==========================================================

st.subheader("📍 Top Pickup Zones")

pickup_df = spark_to_pandas(
    analytics.top_pickup_zones()
)

st.plotly_chart(
    DashboardCharts.pickup_chart(
        pickup_df.head(10)
    ),
    width="stretch"
)

# ==========================================================
# Dropoff Zones
# ==========================================================

st.subheader("📍 Top Dropoff Zones")

dropoff_df = spark_to_pandas(
    analytics.top_dropoff_zones()
)

st.plotly_chart(
    DashboardCharts.dropoff_chart(
        dropoff_df.head(10)
    ),
    width="stretch"
)

# ==========================================================
# Raw Tables
# ==========================================================

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("Top Pickup Zones")

    st.dataframe(
        pickup_df.head(10),
        width="stretch"
    )

with col2:

    st.subheader("Top Dropoff Zones")

    st.dataframe(
        dropoff_df.head(10),
        width="stretch"
    )

# ==========================================================
# Footer
# ==========================================================

st.divider()

st.caption(
    "Built using Apache Spark • PySpark • Streamlit • Plotly"
)

# ==========================================================
# Stop Spark Session
# ==========================================================

# Do NOT stop the Spark session here because it is cached

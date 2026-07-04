# 🚖 Big Data Taxi Analytics Platform

A Big Data Analytics platform built using **Apache Spark (PySpark)** and **Streamlit** to process and visualize NYC Yellow Taxi trip records.

The project demonstrates a complete data analytics workflow including data loading, cleaning, feature engineering, business analytics, and interactive dashboard visualization using Apache Spark.

---

# Project Overview

This project processes NYC Yellow Taxi trip data stored in Parquet format using Apache Spark.

The processed data is analyzed to generate business insights such as:

- Total Trips
- Total Revenue
- Average Fare
- Average Trip Distance
- Peak Pickup Hours
- Payment Distribution
- Top Pickup Zones
- Top Drop-off Zones

The results are presented through an interactive Streamlit dashboard.

---

# Features

- Apache Spark based data processing
- ETL (Extract, Transform, Load) pipeline
- Data Cleaning
- Feature Engineering
- Taxi Zone Lookup Table Join
- Spark DataFrame Caching
- Interactive Dashboard using Streamlit
- Plotly Visualizations
- Modular Project Structure
- Docker Support

---

# Project Structure

```
big-data-taxi-analytics/

│
├── dashboard/
│   ├── app.py
│   ├── charts.py
│   └── dashboard_utils.py
│
├── spark/
│   ├── analytics.py
│   ├── cache_manager.py
│   ├── clean_data.py
│   ├── join_lookup.py
│   ├── load_data.py
│   ├── transform.py
│   └── spark_session.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run_pipeline.py
├── README.md
└── .gitignore
```

---

# Technologies Used

- Python
- Apache Spark (PySpark)
- Streamlit
- Plotly
- Pandas
- PyArrow
- Docker
- Git
- GitHub

---

# Dataset

Dataset:

NYC Yellow Taxi Trip Records

Official Source:

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

Taxi Zone Lookup Table:

https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv

The dataset is **not included** in this repository due to its size.

Place the downloaded files inside:

```
data/raw/
```

Example:

```
data/raw/

yellow_tripdata_2026-01.parquet

taxi_zone_lookup.csv
```

---

# Data Processing Pipeline

```
NYC Taxi Dataset
        │
        ▼
Load Parquet File
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Join Taxi Zone Lookup Table
        │
        ▼
Cache DataFrame
        │
        ▼
Business Analytics
        │
        ▼
Interactive Dashboard
```

---

# Dashboard Metrics

The dashboard displays:

- Total Trips
- Total Revenue
- Average Fare
- Average Trip Distance

---

# Analytics Included

### Peak Pickup Hours

Shows the number of taxi trips grouped by pickup hour.

### Payment Distribution

Displays the distribution of payment types used by passengers.

### Top Pickup Zones

Shows the taxi pickup locations with the highest number of trips.

### Top Drop-off Zones

Shows the taxi drop-off locations with the highest number of trips.

### Summary Tables

Displays tabular summaries of the top pickup and drop-off zones.

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/big-data-taxi-analytics.git

cd big-data-taxi-analytics
```

Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Spark Pipeline

```bash
python run_pipeline.py
```

---

# Run the Dashboard

```bash
streamlit run dashboard/app.py
```

Open

```
http://localhost:8501
```

---

# Docker

Build Docker Image

```bash
docker build -t taxi-analytics .
```

Run Docker Container

```bash
docker run -p 8501:8501 taxi-analytics

---

# Future Improvements

Possible future enhancements include:

- Process multiple months of taxi trip data
- Additional business analytics
- Interactive dashboard filters
- Export analytics reports
- Cloud deployment
- Real-time streaming using Spark Structured Streaming

This project is licensed under the MIT License.

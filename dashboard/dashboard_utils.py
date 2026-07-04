import pandas as pd


def spark_to_pandas(df):

    """
    Convert Spark DataFrame to Pandas DataFrame.
    """

    return df.toPandas()
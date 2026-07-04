from pyspark.sql import DataFrame


class CacheManager:
    """
    Utility class for caching and uncaching Spark DataFrames.
    """

    @staticmethod
    def cache(df: DataFrame) -> DataFrame:
        """
        Cache a Spark DataFrame in memory.

        Parameters
        ----------
        df : DataFrame
            Spark DataFrame to cache.

        Returns
        -------
        DataFrame
            Cached Spark DataFrame.
        """

        print("=" * 60)
        print("Caching Spark DataFrame...")
        print("=" * 60)

        # Cache DataFrame
        cached_df = df.cache()

        # Materialize cache immediately
        cached_df.count()

        print("DataFrame cached successfully.\n")

        return cached_df

    @staticmethod
    def uncache(df: DataFrame) -> None:
        """
        Remove a cached DataFrame from memory.

        Parameters
        ----------
        df : DataFrame
            Cached Spark DataFrame.
        """

        print("=" * 60)
        print("Removing Spark DataFrame from cache...")
        print("=" * 60)

        df.unpersist()

        print("Cache removed successfully.\n")
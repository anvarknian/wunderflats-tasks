from pyspark.sql import SparkSession


def spark_factory(app_name: str):
    spark = SparkSession \
        .builder \
        .appName(app_name) \
        .master('local[*]') \
        .config('spark.sql.warehouse.dir', 'file:///') \
        .config('spark.driver.memory', '10g') \
        .config('spark.driver.host', '127.0.0.1') \
        .config('spark.driver.bindAddress', '127.0.0.1') \
        .config('spark.executor.memory', '10g') \
        .getOrCreate()
    return spark

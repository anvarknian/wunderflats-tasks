from pyspark.sql import SparkSession
import google.cloud.bigquery as bq

def bq_factory():
    return bq.Client()


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


def insert_data(client):
    client.insert_rows(client.get_table("myproject.mydataset.mytable"), data)


if __name__ == '__main__':
    spark = spark_factory('SPARK_JOB')
    data = spark.read \
        .option('delimiter', ',') \
        .option('inferSchema', 'true') \
        .option('header', 'true') \
        .csv('myfile.csv')

    # # Checking Schema of DF
    # data.printSchema()
    # # Checking DF
    # data.show(5)



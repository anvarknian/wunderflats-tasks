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


def spark_runner():
    spark = spark_factory('SPARK_JOB')

    data = spark.read \
        .option('delimiter', ',') \
        .option('inferSchema', True) \
        .option('header', 'true') \
        .csv('resources/myfile.csv')

    # # Checking Schema of DF
    data.printSchema()
    # # Checking DF
    data.show(5)

    data.write \
        .option('header', True) \
        .partitionBy('Home State') \
        .format('bigquery') \
        .option('table', 'myproject.mydataset.mytable').mode('append').save()

    return "OK"

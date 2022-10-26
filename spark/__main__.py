from spark.main import spark_factory

if __name__ == '__main__':

    spark = spark_factory('SPARK_JOB')

    data = spark.read \
        .option('delimiter', ',') \
        .option('inferSchema', True) \
        .option('header', 'true') \
        .csv('resources/myfile.csv')

    # # Checking Schema of DF
    # data.printSchema()
    # # Checking DF
    # data.show(5)

    data.write \
        .option('header', True) \
        .partitionBy('Home State') \
        .format('bigquery') \
        .option('table', 'myproject.mydataset.mytable').mode('append').save()

from pyspark.sql import SparkSession

def spark():
    spark=SparkSession.builder.appName("OrdersDBDataProcessing").\
    config("spark.sql.warehouse.dir","hdfs://localhost:9090/user/hive/wherehouse").\
    master("local").\
    getOrCreate()
    return spark
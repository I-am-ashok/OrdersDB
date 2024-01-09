from pyspark.sql import SparkSession

def spark():
    spark=SparkSession.builder.appName("OrdersDBDataProcessing").\
    config("spark.sql.warehouse.dir","hdfs://gcpsparkcluster-m/user/hive/warehouse").\
    master("local").\
    getOrCreate()
    return spark
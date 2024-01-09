from Trasformations import *
from SparkSession import *
def savedata(df):
    df.write.saveAsTable("ordersdb.Orders",format="parquet",mode="overwrite")
    return spark().sql("select count(*) as reccount from ordersdb.Orders")
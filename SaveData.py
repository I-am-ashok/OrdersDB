from Trasformations import *
def savedata(): 
    Transformationsdf().write.saveAsTable("ordersdb.Orders",format="parquet",mode="overwrite")
    return spark.sql("select count(*) as reccount from ordersdb.Orders")
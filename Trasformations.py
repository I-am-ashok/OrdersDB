from Dataload import *
from pyspark.sql.functions import *

def Transformationsdf(df1,df2):
    txdf=df1.withColumn("YearMonth",date_format("order_date","yyyyMM").cast('int')).\
        withColumn("Year",year("order_date").cast('int')).\
        withColumn("Date",date_format("order_date","yyyy-MM-dd").cast('date')).drop("order_date")
    txdf=txdf.join(df2,on=txdf["order_id"]==df2["order_item_order_id"],how="inner").\
        select(txdf["*"],
               df2["order_item_product_id"],
               df2["order_item_product_price"],
               df2["order_item_quantity"],
               df2["order_item_subtotal"])
    return txdf
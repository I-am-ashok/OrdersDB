This is complete end to end pyspark project implementation project. 
our goal is to extract data from json and applying some trasformations then load the data into hive table (orders)

to achive it we used 
1. Visual studio code to develop the pyspark code
2. git as a version control and repository
3. DataProc as Spark cluster with one master node n2-standard-4core

develop the code using pyspark api as mentioned in this repository then zip te files to submit to spark.
   To zip the files
#Compress-Archive -Path OrdersDB\* -DestinationPath ordersdb.zip
To update the files in zip file
#Compress-Archive -Path .\Config\variable.txt -Update -DestinationPath .\ordersdb.zip

#create Local directory in the masterNode
# mkdir PYSPARK/OrdersDB

# copy local directory to HDFS

HDFS dfs -copyFromLocal /user/mashok4102/PYSPARK/OrdersDB/* HDFS://masterNode/user/mashok4102/PYSPARK/OrdersDB


then submit the zip to spark like 

spark-submit --deploy-mode client --master local --py-files ordersdb.zip main.py


then check the DB and table in hive and confirm the data. 


spark

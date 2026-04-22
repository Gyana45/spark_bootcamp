from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
spark = SparkSession\
                    .builder\
                    .master("spark://spark-master:7077")\
                    .appName("Day_9_AQE")\
                    .config("spark.sql.warehouse.dir", "/data/spark-warehouse")\
                    .enableHiveSupport()\
                    .getOrCreate()

orders_schema_struct = StructType(
                                    [
                                        StructField("order_id",IntegerType()),
                                        StructField("customer_id",IntegerType()),
                                        StructField("product_id",IntegerType()),
                                        StructField("price",FloatType()),
                                        StructField("order_date",DateType()),
                                        StructField("order_status",StringType()),
                                        StructField("state",StringType()),
                                        StructField("quantity",IntegerType()),
                                    ]
                                )

df_orders = spark.read.csv('/data/orders_1gb.csv',schema=orders_schema_struct,header=True)

df_orders.show(5)
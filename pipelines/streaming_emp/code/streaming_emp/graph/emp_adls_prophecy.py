from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from streaming_emp.config.ConfigStore import *
from streaming_emp.udfs.UDFs import *

def emp_adls_prophecy(spark: SparkSession, in0: DataFrame):
    in0.writeStream\
        .format("delta")\
        .option("checkpointLocation", "/tmp/_checkpoint/prophecy/auto_loader_emp")\
        .queryName("emp_adls_prophecy_L1KpmEBeSZol5McCyZO9r$$yaRt5537tquerYfJ1XUp5")\
        .outputMode("append")\
        .trigger(once = True)\
        .start("abfss://external-locations@juanstgaccntusw2.dfs.core.windows.net/prophecy_tables/emp")

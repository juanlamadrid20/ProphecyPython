from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from streaming_emp.config.ConfigStore import *
from streaming_emp.udfs.UDFs import *

def emp_adls(spark: SparkSession) -> DataFrame:
    return spark.readStream\
        .format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
        .option("header", True)\
        .option("sep", ",")\
        .schema(
          StructType([
            StructField("fname", StringType(), True), StructField("lname", StringType(), True), StructField("employer_id", StringType(), True), StructField("ssn", StringType(), True), StructField("weight_lb", StringType(), True), StructField("height_in", StringType(), True), StructField("gender", StringType(), True), StructField("righty", StringType(), True), StructField("hire_date", StringType(), True), StructField("state", StringType(), True)
        ])
        )\
        .load("abfss://external-locations@juanstgaccntusw2.dfs.core.windows.net/landing/emp")

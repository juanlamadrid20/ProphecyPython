from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *
from prophecy.utils import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Orders = Orders(spark)
    df_Customers = Customers(spark)
    df_By_CustomerId = By_CustomerId(spark, df_Orders, df_Customers)
    df_Subgraph_1 = Subgraph_1(spark, df_By_CustomerId)
    Customer_Orders(spark, df_Subgraph_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/customers_orders")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/customers_orders")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()

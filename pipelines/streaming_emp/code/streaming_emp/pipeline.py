from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from streaming_emp.config.ConfigStore import *
from streaming_emp.udfs.UDFs import *
from prophecy.utils import *
from streaming_emp.graph import *

def pipeline(spark: SparkSession) -> None:
    df_emp_adls = emp_adls(spark)
    emp_adls_prophecy(spark, df_emp_adls)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/streaming_emp")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/streaming_emp")
    pipeline(spark)
    
    spark.streams.resetTerminated()
    spark.streams.awaitAnyTermination()
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()

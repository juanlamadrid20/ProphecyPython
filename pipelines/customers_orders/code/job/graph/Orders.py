from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Orders(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"juan_ct_external.default.emp_auto_loader_bz_tbl")

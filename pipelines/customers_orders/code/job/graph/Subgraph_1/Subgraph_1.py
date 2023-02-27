from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *

def Subgraph_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df_Cleanup_1 = Cleanup_1(spark, in0)
    df_Sum_Amounts_1 = Sum_Amounts_1(spark, df_Cleanup_1)

    return df_Sum_Amounts_1

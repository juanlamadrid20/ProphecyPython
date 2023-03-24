from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Cleanup_1 = Cleanup_1(spark, in0)
    df_Sum_Amounts_1 = Sum_Amounts_1(spark, df_Cleanup_1)

    return df_Sum_Amounts_1

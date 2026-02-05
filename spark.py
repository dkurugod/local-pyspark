import sys
from pyspark.sql import SparkSession

print("Python executable:", sys.executable)

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("final-test") \
    .getOrCreate()

spark.range(5).show()

spark.stop()

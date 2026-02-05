from pyspark.sql import SparkSession 

spark = SparkSession.builder.appName("demo").getOrCreate() 

df = spark.createDataFrame( 
    
    [("Alice", 34), ("Bob", 45), ("Cathy", 29)], 
    ["Name", "Age"] ) 

df.show()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def run_etl():
    spark = SparkSession.builder.appName('MovieETL').getOrCreate()
    # Example: Read CSV, simple transformation, write back
    df = spark.read.csv('../data/ratings.csv', header=True, inferSchema=True)
    df = df.filter(col('rating') >= 3)
    df.write.csv('../data/ratings_filtered.csv', header=True, mode='overwrite')
    spark.stop()

if __name__ == "__main__":
    run_etl()
    print('ETL pipeline complete (PySpark).')

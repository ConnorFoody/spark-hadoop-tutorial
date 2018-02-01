from pyspark.sql import SparkSession
import sys

if __name__ == "__main__":
    spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    splits = lines.flatMap(lambda x: x.split(' '))
    ones = splits.map(lambda x: (x, 1))
    counts = ones.reduceByKey(lambda x, y: x + y)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))
    spark.stop()

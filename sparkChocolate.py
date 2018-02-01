from __future__ import print_function 

import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":

    spark = SparkSession\
            .builder\
            .appName("PythonWordCount")\
            .getOrCreate()
    lines = spark.read.format("csv").option("header", "true").load(sys.argv[1])
    lines.show()
    makers = lines.select("Company").rdd
    makersMap = makers.map(lambda x: (x, 1))
    makersCount = makersMap.reduceByKey(lambda x, y: x+y)
    output = makersCount.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))
    spark.stop()

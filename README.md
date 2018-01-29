# spark-hadoop-tutorial

### Setting up docker image
We are using a prebuilt docker image from [here](https://github.com/sequenceiq/docker-spark). Get the image by runnning:  
```docker pull sequenceiq/spark:1.6.0```

Spin up the container and enter its shell with the command:   
```docker run -it -p 8088:8088 -p 8042:8042 -p 4040:4040 -h sandbox sequenceiq/spark:1.6.0 bash```

The spark directory is located at ```~/usr/local/spark```. To test that spark is set up correctly, run:  
```./bin/spark-submit --class org.apache.spark.examples.SparkPi lib/spark-examples-1.6.0-hadoop2.6.0.jar```

### Using hadoop
To copy a file to hadoop, enter ```hadoop fs -copyFromLocal <path to local file> <path in hdfs>```. Note: to access hadoop from spark, use the path ```hdfs:/<path>```, don't use the ```hdfs://``` notation unless you want to explicitly specify where your hdfs instance is. 

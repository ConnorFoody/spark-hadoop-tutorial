# spark-hadoop-tutorial

### Setting up docker image
You can get our docker image from here:  
```docker pull cfoody/spark-hadoop-tutorial:firsttry``` 

You can then run our image using   
```docker run -it -p 8088:8088 -p 8042:8042 -p 4040:4040 -h sandbox cfoody/spark-hadoop-tutorial:firsttry bash```

You may need to run these commands as root. 

### Using hadoop
To copy a file to hadoop, enter ```hadoop fs -copyFromLocal <path to local file> <path in hdfs>```. Note: to access hadoop from spark, use the path ```hdfs:/<path>```, don't use the ```hdfs://``` notation unless you want to explicitly specify where your hdfs instance is. 

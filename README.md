# spark-hadoop-tutorial

### Setting up docker image
You can get our docker image from here:  
```docker pull cfoody/spark-hadoop-tutorial``` 

You can then run our image using:   
```docker run -it -p 8088:8088 -p 8042:8042 -p 4040:4040 -h sandbox cfoody/spark-hadoop-tutorial bash```

In /usr/local/tutorial you will find all the files you need plus some useful scripts. 

### Helpful Docker tips

You can find the container id with ```docker ps```   

Copy a file to docker with ```docker cp <local file> <container id>:<container filepath>```


Open another terminal into container: ```docker exec -it <container id> bash```  

    
You may need to run these commands as root. 

### Using Hadoop
To copy a file to hadoop, enter ```hadoop fs -copyFromLocal <path to local file> <path in hdfs>```. The ```hadoop fs``` command also provides several other options including ```-ls```, ```-cat``` etc

Compile the java file. Note that you should have an output folder, in this case called "output":   
```javac -classpath $(hadoop classpath) -d output WordCount.java```

Create jar file: ```jar -cvf wordcount.jar -C output/ .``` 

Run: ```hadoop jar wc.jar WordCount <the file you put into hdfs> dft-output``` 

Kill: ```hadoop job -kill job_id``` 

Print out output: ```hadoop fs -cat dft-output/part-r-00000 | less``` 

Copy to local: ```hadoop fs -copyToLocal dft-output/part-r-00000``` 

Remove directory: ```hadoop dfs -rm -r dft-output``` 


### Using Spark
Note: to access hadoop from spark, use the path ```hdfs:/<path>```, don't use the ```hdfs://``` notation unless you want to explicitly specify where your hdfs instance is. 

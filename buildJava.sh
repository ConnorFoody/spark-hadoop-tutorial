#!/bin/bash
rm -rf output
mkdir output

javac -classpath $(hadoop classpath) -d output WordCount.java
jar -cvf wordcount.jar -C output/ .
hadoop jar wordcount.jar WordCount $1 dft-output

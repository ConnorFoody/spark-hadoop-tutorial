FROM cfoody/spark-hadoop-updated

COPY .vimrc /root/.vimrc
COPY spark-hadoop-tutorial /usr/local/tutorial
RUN sed -i 's/[\d128-\d255]//g' /usr/local/tutorial/cacao.csv
RUN chmod +x /usr/local/tutorial/*.sh

RUN yum clean all; yum -y install numpy; yum clean all; yum -y install nano; yum clean all

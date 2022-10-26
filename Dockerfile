ARG OPENJDK_VERSION=8
ARG DEBIAN_RELEASE=""
FROM openjdk:${OPENJDK_VERSION}-jre-slim${DEBIAN_RELEASE} as base

ARG SPARK_VERSION=3.0.0

LABEL org.opencontainers.image.title="Apache PySpark $SPARK_VERSION" \
   org.opencontainers.image.version=$SPARK_VERSION

ENV PATH="/opt/miniconda3/bin:${PATH}"
ENV PYSPARK_PYTHON="/opt/miniconda3/bin/python"

RUN set -ex
RUN	apt-get update
RUN apt-get install -y curl bzip2 --no-install-recommends
RUN curl -s -L --url "https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh" --output /tmp/miniconda.sh
RUN bash /tmp/miniconda.sh -b -f -p "/opt/miniconda3"
RUN rm /tmp/miniconda.sh
RUN conda config --set auto_update_conda true
RUN conda config --set channel_priority false
RUN conda update conda -y --force-reinstall
RUN conda install pip
RUN conda clean -tipy
RUN echo "PATH=/opt/miniconda3/bin:\${PATH}" > /etc/profile.d/miniconda.sh
RUN pip install --no-cache pyspark[$SPARK_EXTRAS]==${SPARK_VERSION}
RUN SPARK_HOME=$(python /opt/miniconda3/bin/find_spark_home.py)
RUN echo "export SPARK_HOME=$(python /opt/miniconda3/bin/find_spark_home.py)" > /etc/profile.d/spark.sh
RUN curl -s -L --url "https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-java-sdk-1.7.4.jar" --output $SPARK_HOME/jars/aws-java-sdk-1.7.4.jar
RUN curl -s -L --url "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.7.3/hadoop-aws-2.7.3.jar" --output $SPARK_HOME/jars/hadoop-aws-2.7.3.jar
RUN curl -s -L --url "https://repo1.maven.org/maven2/io/delta/delta-core_2.12/1.0.0/delta-core_2.12-1.0.0.jar" --output $SPARK_HOME/jars/delta-core_2.12-1.0.0.jar
RUN mkdir -p $SPARK_HOME/conf
RUN echo "spark.hadoop.fs.s3.impl=org.apache.hadoop.fs.s3a.S3AFileSystem" >> $SPARK_HOME/conf/spark-defaults.conf
RUN apt-get remove -y curl bzip2
RUN apt-get autoremove -y
RUN apt-get clean

FROM base AS dev
# Project initialization:
RUN pip install -r /app/requirements.txt

FROM dev AS stage
# Creating folders, and files for a project:
COPY . /app
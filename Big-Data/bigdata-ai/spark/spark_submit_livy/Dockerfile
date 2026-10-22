FROM apache/spark:3.5.8

USER root

# 1. Install dependencies
RUN apt-get update && apt-get install -y curl unzip python3-pip && rm -rf /var/lib/apt/lists/*

# 2. Download and extract Livy 0.9.0 (Scala 2.12 version)
ENV LIVY_HOME /opt/livy
RUN curl -fSL https://dlcdn.apache.org/incubator/livy/0.9.0-incubating/apache-livy-0.9.0-incubating_2.12-bin.zip -o livy.zip \
    && unzip livy.zip -d /opt \
    && mv /opt/apache-livy-0.9.0-incubating_2.12-bin /opt/livy \
    && rm livy.zip

# 3. Set environment variables
ENV SPARK_HOME /opt/spark
ENV PATH $PATH:/opt/livy/bin
WORKDIR /opt/livy

# Ensure logs directory exists
RUN mkdir -p /opt/livy/logs

EXPOSE 8998

# Start Livy in the foreground
CMD ["livy-server"]

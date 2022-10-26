FROM python:3.9-buster
RUN apt update
RUN apt install openjdk-11-jdk openjdk-11-source -y
RUN java --version
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN python --version
RUN pip install -r /app/requirements.txt
RUN spark-submit --version

FROM arm32v7/python:3.7.4-slim
# FROM arm32v7/debian:stretch-slim 


ENV PYTHONUNBUFFERED 1

COPY qemu-arm-static /usr/bin/qemu-arm-static

RUN mkdir /code

WORKDIR /code

COPY requeriments.txt /code/

RUN apt-get update

RUN apt-get install -y gcc g++ python3-psycopg2 libpq-dev

RUN pip install -r requeriments.txt

RUN apt-get clean && apt-get purge -y gcc g++ && apt-get autoremove -y

COPY . /code/

FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requeriments.txt /code/

RUN apt-get update

RUN apt-get install -y python3.7-dev python3-psycopg2 libpq-dev

RUN pip install -r requeriments.txt

COPY . /code/

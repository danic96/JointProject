FROM python:3.7.3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requeriments.txt /code/

RUN pip install -r requeriments.txt

COPY . /code/

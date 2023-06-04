FROM python:3.8

ENV PYTHONUNBUFFERED 1

USER root
RUN apt-get update && apt-get install -y gdal-bin

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
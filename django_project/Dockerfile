# syntax=docker/dockerfile:1
FROM python:3
ENV C:\Users\31010-12-05\AppData\Local\Programs\Python\Python310=1
WORKDIR /django_project
COPY requirements.txt /django_project/
RUN pip install -r requirements.txt
COPY . /django_project/
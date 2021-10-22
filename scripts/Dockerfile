# Multistage Docker build
# syntax=docker/dockerfile:1
# first stage build
FROM python:3.8 AS test
WORKDIR /code
COPY web_app .


# second stage build
FROM python:3.8 AS debug
RUN mkdir app
WORKDIR /app
# install dependencies 
# RUN apt-get update -y && apt-get install redis libssl-dev -y 
RUN apt-get install libssl-dev -y 
RUN pip install --upgrade pip
COPY --from=0 /code/requirements.txt .
RUN pip install -r requirements.txt
COPY --from=0 /code/ .
RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 8000
CMD python manage.py runserver




# # Multistage Docker build
# # syntax=docker/dockerfile:1
# # first stage build
# FROM ubuntu:latest AS test
# RUN mkdir code
# WORKDIR /code
# COPY web_app .


# # second stage build
# FROM ubuntu:latest AS debug
# RUN mkdir app
# WORKDIR /app
# # install dependencies 
# RUN apt-get update -y && apt-get install libssl-dev -y
# RUN apt-get install python3-pip -y
# RUN pip install --upgrade pip
# COPY --from=0 /code/requirements.txt .
# RUN pip install -r requirements.txt
# COPY --from=0 /code/ .
# EXPOSE 8000
# CMD python manage.py runserver

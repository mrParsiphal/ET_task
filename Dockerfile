FROM python:latest


MAINTAINER MrParsiphal


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ="Europe/Moscow"


RUN pip install django
RUN pip install gunicorn


EXPOSE 80
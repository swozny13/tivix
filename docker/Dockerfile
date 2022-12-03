FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /project/app

COPY requirements.txt /project/app

RUN pip install -r requirements.txt

COPY . /project/app

EXPOSE 8000
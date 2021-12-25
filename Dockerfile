FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE true
ENV PYTHONUNBUFFERED true

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
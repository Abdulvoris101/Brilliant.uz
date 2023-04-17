FROM python:3-alpine

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY ./req.txt /app/

RUN pip install -r req.txt

COPY . /app

COPY start_prod.sh /app/

RUN chmod +x start_prod.sh



from python:3.8.0-alpine3.10

WORKDIR /twilio-services

ENV FLASK_APP app.py

RUN apk add --no-cache bash

COPY configs configs
COPY src src
COPY app.py app.py
COPY requires.txt requires.txt
COPY configs configs

RUN pip install -r requires.txt

CMD ["python", "app.py"]

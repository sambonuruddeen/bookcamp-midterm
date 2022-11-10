FROM python:3.10-slim-buster

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"]
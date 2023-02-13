FROM python:3.8-slim

WORKDIR /app

COPY stripe_pay/ .

COPY requirements.txt /app

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

ENTRYPOINT ["bash", "docker-entrypoint.sh"]

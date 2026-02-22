FROM python:3.11-alpine

WORKDIR /app

COPY ./requirements.txt /gateway/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /gateway/requirements.txt

COPY . /app/gateway

ENV PYTHONPATH=/app

ENV PROD_ENV="prod"

CMD ["uvicorn", "gateway.main:app", "--host", "0.0.0.0", "--port", "10000", "--reload"]
FROM python:3.11-alpine

WORKDIR /app

COPY ./requirements.txt /url_shortener_service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /url_shortener_service/requirements.txt

COPY . /app/url_shortener_service

ENV PYTHONPATH=/app

ENV PROD_ENV="prod"

CMD ["uvicorn", "url_shortener_service.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
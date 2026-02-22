FROM python:3.11-alpine

WORKDIR /app

COPY ./requirements.txt /auth_service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /auth_service/requirements.txt

COPY . /app/auth_service

ENV PYTHONPATH=/app

ENV PROD_ENV="prod"

CMD ["uvicorn", "auth_service.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
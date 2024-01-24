FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn requests openap

EXPOSE 8610

CMD [ "uvicorn", "svcinvest.main:app", "--host", "0.0.0.0", "--port", "8610", "--root-path", "/api/v1"]


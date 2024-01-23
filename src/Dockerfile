FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn requests openap

EXPOSE 80

CMD [ "uvicorn", "svcinvest.main:app", "--host", "0.0.0.0", "--port", "5000" ]


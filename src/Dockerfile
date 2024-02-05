FROM python:3.10

WORKDIR /app

COPY . /app

# RUN pip install --no-cache-dir fastapi uvicorn requests openap
RUN pip install -r requirements.txt

EXPOSE 8610

CMD [ "uvicorn", "svcinvest.apiLayer.main:app", "--host", "0.0.0.0", "--port", "8610", "--root-path", "/api/v1"]

